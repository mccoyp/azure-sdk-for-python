from typing import List, Dict, Union
import json
import math
import os
import pathlib
import numpy as np
from unittest.mock import patch

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
import test
from azure.ai.evaluation._legacy._adapters.client import PFClient

from azure.ai.evaluation._common.math import list_mean
from azure.ai.evaluation import (
    ContentSafetyEvaluator,
    F1ScoreEvaluator,
    GroundednessEvaluator,
    SimilarityEvaluator,
    ProtectedMaterialEvaluator,
    evaluate,
    ViolenceEvaluator,
    SexualEvaluator,
    SelfHarmEvaluator,
    HateUnfairnessEvaluator,
)
from azure.ai.evaluation._constants import (
    DEFAULT_EVALUATION_RESULTS_FILE_NAME,
    _AggregationType,
    EvaluationRunProperties,
)
from azure.ai.evaluation._evaluate._evaluate import (
    _aggregate_metrics,
    _apply_target_to_data,
    _rename_columns_conditionally,
)
from azure.ai.evaluation._evaluate._utils import _convert_name_map_into_property_entries
from azure.ai.evaluation._evaluate._utils import _apply_column_mapping, _trace_destination_from_project_scope
from azure.ai.evaluation._evaluators._eci._eci import ECIEvaluator
from azure.ai.evaluation._exceptions import EvaluationException


def _get_file(name):
    """Get the file from the unittest data folder."""
    data_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "data")
    return os.path.join(data_path, name)


@pytest.fixture
def unsupported_file_type():
    return _get_file("unsupported_file_type.txt")


@pytest.fixture
def missing_header_csv_file():
    return _get_file("no_header_evaluate_test_data.csv")


@pytest.fixture
def invalid_jsonl_file():
    return _get_file("invalid_evaluate_test_data.jsonl")


@pytest.fixture
def missing_columns_jsonl_file():
    return _get_file("missing_columns_evaluate_test_data.jsonl")


@pytest.fixture
def evaluate_test_data_jsonl_file():
    return _get_file("evaluate_test_data.jsonl")


@pytest.fixture
def evaluate_test_data_conversion_jsonl_file():
    return _get_file("evaluate_test_data_conversation.jsonl")


@pytest.fixture
def evaluate_test_data_alphanumeric():
    return _get_file("evaluate_test_data_alphanumeric.jsonl")


@pytest.fixture
def questions_file():
    return _get_file("questions.jsonl")


@pytest.fixture
def questions_wrong_file():
    return _get_file("questions_wrong.jsonl")


@pytest.fixture
def questions_answers_file():
    return _get_file("questions_answers.jsonl")


@pytest.fixture
def questions_answers_basic_file():
    return _get_file("questions_answers_basic.jsonl")


@pytest.fixture
def questions_answers_korean_file():
    return _get_file("questions_answers_korean.jsonl")


@pytest.fixture
def restore_env_vars():
    """Fixture to restore environment variables after the test."""
    original_vars = os.environ.copy()
    yield
    os.environ.clear()
    os.environ.update(original_vars)


def _target_fn(query):
    """An example target function."""
    if "LV-426" in query:
        return {"response": "There is nothing good there."}
    if "central heating" in query:
        return {"response": "There is no central heating on the streets today, but it will be, I promise."}
    if "strange" in query:
        return {"response": "The life is strange..."}


def _yeti_evaluator(query, response):
    if "yeti" in query.lower():
        raise ValueError("Do not ask about Yeti!")
    return {"result": len(response)}


def _target_fn2(query):
    response = _target_fn(query)
    response["query"] = f"The query is as follows: {query}"
    return response


def _target_that_fails(query):
    raise Exception("I am failing")


def _new_answer_target():
    return {"response": "new response"}


def _question_override_target(query):
    return {"query": "new query"}


def _question_answer_override_target(query, response):
    return {"query": "new query", "response": "new response"}


@pytest.mark.usefixtures("mock_model_config")
@pytest.mark.unittest
class TestEvaluate:
    def test_evaluate_evaluators_not_a_dict(self, mock_model_config, questions_file):
        with pytest.raises(EvaluationException) as exc_info:
            evaluate(
                data=questions_file,
                evaluators=[GroundednessEvaluator(model_config=mock_model_config)],
            )

        assert "The 'evaluators' parameter must be a dictionary." in exc_info.value.args[0]

    def test_evaluate_invalid_data(self, mock_model_config):
        with pytest.raises(EvaluationException) as exc_info:
            evaluate(
                data=123,
                evaluators={"g": GroundednessEvaluator(model_config=mock_model_config)},
            )

        assert "The 'data' parameter must be a string or a path-like object." in exc_info.value.args[0]

    def test_evaluate_data_not_exist(self, mock_model_config):
        with pytest.raises(EvaluationException) as exc_info:
            evaluate(
                data="not_exist.jsonl",
                evaluators={"g": GroundednessEvaluator(model_config=mock_model_config)},
            )

        assert "The input data file path 'not_exist.jsonl' does not exist." in exc_info.value.args[0]

    def test_target_not_callable(self, mock_model_config, questions_file):
        with pytest.raises(EvaluationException) as exc_info:
            evaluate(
                data=questions_file,
                evaluators={"g": GroundednessEvaluator(model_config=mock_model_config)},
                target="not_callable",
            )

        assert "The 'target' parameter must be a callable function." in exc_info.value.args[0]

    def test_evaluate_invalid_jsonl_data(self, mock_model_config, invalid_jsonl_file):
        with pytest.raises(EvaluationException) as exc_info:
            evaluate(
                data=invalid_jsonl_file,
                evaluators={"g": GroundednessEvaluator(model_config=mock_model_config)},
            )

        assert "Unable to load data from " in exc_info.value.args[0]
        assert "Supported formats are JSONL and CSV. Detailed error:" in exc_info.value.args[0]

    def test_evaluate_missing_required_inputs(self, missing_columns_jsonl_file):
        with pytest.raises(EvaluationException) as exc_info:
            evaluate(
                data=missing_columns_jsonl_file, evaluators={"g": F1ScoreEvaluator()}, fail_on_evaluator_errors=True
            )
        expected_message = "Either 'conversation' or individual inputs must be provided."
        assert expected_message in exc_info.value.args[0]
        # Same call without failure flag shouldn't produce an exception.
        evaluate(data=missing_columns_jsonl_file, evaluators={"g": F1ScoreEvaluator()})

    def test_evaluate_missing_required_inputs_target(self, questions_wrong_file):
        with pytest.raises(EvaluationException) as exc_info:
            evaluate(data=questions_wrong_file, evaluators={"g": F1ScoreEvaluator()}, target=_target_fn)
        assert "Missing required inputs for target: ['query']." in exc_info.value.args[0]

    def test_target_not_generate_required_columns(self, questions_file):
        with pytest.raises(EvaluationException) as exc_info:
            # target_fn will generate the "response", but not "ground_truth".
            evaluate(
                data=questions_file,
                evaluators={"g": F1ScoreEvaluator()},
                target=_target_fn,
                fail_on_evaluator_errors=True,
            )

        expected_message = "Either 'conversation' or individual inputs must be provided."

        assert expected_message in exc_info.value.args[0]

        # Same call without failure flag shouldn't produce an exception.
        evaluate(data=questions_file, evaluators={"g": F1ScoreEvaluator()}, target=_target_fn)

    def test_target_raises_on_outputs(self):
        """Test we are raising exception if the output is column is present in the input."""
        data = _get_file("questions_answers_outputs.jsonl")
        with pytest.raises(EvaluationException) as cm:
            evaluate(
                data=data,
                target=_target_fn,
                evaluators={"g": F1ScoreEvaluator()},
            )
        assert 'The column cannot start from "__outputs." if target was defined.' in cm.value.args[0]

    @pytest.mark.parametrize(
        "input_file,out_file,expected_columns,fun",
        [
            ("questions.jsonl", "questions_answers.jsonl", {"response"}, _target_fn),
            (
                "questions_ground_truth.jsonl",
                "questions_answers_ground_truth.jsonl",
                {"response", "query"},
                _target_fn2,
            ),
        ],
    )
    @pytest.mark.skip(reason="Breaking CI by crashing pytest somehow")
    def test_apply_target_to_data(self, pf_client, input_file, out_file, expected_columns, fun):
        """Test that target was applied correctly."""
        data = _get_file(input_file)
        expexted_out = _get_file(out_file)
        initial_data = pd.read_json(data, lines=True)
        qa_df, columns, _ = _apply_target_to_data(fun, data, pf_client, initial_data)
        assert columns == expected_columns
        ground_truth = pd.read_json(expexted_out, lines=True)
        assert_frame_equal(qa_df, ground_truth, check_like=True)

    @pytest.mark.skip(reason="Breaking CI by crashing pytest somehow")
    def test_apply_column_mapping(self):
        json_data = [
            {
                "query": "How are you?",
                "ground_truth": "I'm fine",
            }
        ]
        inputs_mapping = {
            "query": "${data.query}",
            "response": "${data.ground_truth}",
        }

        data_df = pd.DataFrame(json_data)
        new_data_df = _apply_column_mapping(data_df, inputs_mapping)

        assert "query" in new_data_df.columns
        assert "response" in new_data_df.columns

        assert new_data_df["query"][0] == "How are you?"
        assert new_data_df["response"][0] == "I'm fine"

    @pytest.mark.parametrize(
        "json_data,inputs_mapping,response",
        [
            (
                [
                    {
                        "query": "How are you?",
                        "__outputs.response": "I'm fine",
                    }
                ],
                {
                    "query": "${data.query}",
                    "response": "${run.outputs.response}",
                },
                "I'm fine",
            ),
            (
                [
                    {
                        "query": "How are you?",
                        "response": "I'm fine",
                        "__outputs.response": "I'm great",
                    }
                ],
                {
                    "query": "${data.query}",
                    "response": "${run.outputs.response}",
                },
                "I'm great",
            ),
            (
                [
                    {
                        "query": "How are you?",
                        "response": "I'm fine",
                        "__outputs.response": "I'm great",
                    }
                ],
                {
                    "query": "${data.query}",
                    "response": "${data.response}",
                },
                "I'm fine",
            ),
            (
                [
                    {
                        "query": "How are you?",
                        "response": "I'm fine",
                        "__outputs.response": "I'm great",
                    }
                ],
                {
                    "query": "${data.query}",
                    "response": "${data.response}",
                    "another_response": "${run.outputs.response}",
                },
                "I'm fine",
            ),
            (
                [
                    {
                        "query": "How are you?",
                        "response": "I'm fine",
                        "__outputs.response": "I'm great",
                    }
                ],
                {
                    "query": "${data.query}",
                    "response": "${run.outputs.response}",
                    "another_response": "${data.response}",
                },
                "I'm great",
            ),
            (
                [
                    {
                        "query": "How are you?",
                        "__outputs.response": "I'm fine",
                        "else": "Another column",
                        "else1": "Another column 1",
                    }
                ],
                {
                    "query": "${data.query}",
                    "response": "${run.outputs.response}",
                    "else1": "${data.else}",
                    "else2": "${data.else1}",
                },
                "I'm fine",
            ),
        ],
    )
    def test_apply_column_mapping_target(self, json_data, inputs_mapping, response):

        data_df = pd.DataFrame(json_data)
        new_data_df = _apply_column_mapping(data_df, inputs_mapping)

        assert "query" in new_data_df.columns
        assert "response" in new_data_df.columns

        assert new_data_df["query"][0] == "How are you?"
        assert new_data_df["response"][0] == response
        if "another_response" in inputs_mapping:
            assert "another_response" in new_data_df.columns
            assert new_data_df["another_response"][0] != response
        if "else" in inputs_mapping:
            assert "else1" in new_data_df.columns
            assert new_data_df["else1"][0] == "Another column"
            assert "else2" in new_data_df.columns
            assert new_data_df["else2"][0] == "Another column 1"

    @pytest.mark.parametrize(
        "column_mapping",
        [
            {"query": "${foo.query}"},
            {"query": "${data.query"},
            {"query": "data.query", "response": "target.response"},
        ],
    )
    def test_evaluate_invalid_column_mapping(self, mock_model_config, evaluate_test_data_jsonl_file, column_mapping):
        # Invalid source reference
        with pytest.raises(EvaluationException) as exc_info:
            evaluate(
                data=evaluate_test_data_jsonl_file,
                evaluators={"g": GroundednessEvaluator(model_config=mock_model_config)},
                evaluator_config={
                    "g": {
                        "column_mapping": column_mapping,
                    }
                },
            )

        assert (
            "Unexpected references detected in 'column_mapping'. Ensure only ${target.} and ${data.} are used."
            in exc_info.value.args[0]
        )

    def test_evaluate_valid_column_mapping_with_numeric_chars(self, mock_model_config, evaluate_test_data_alphanumeric):
        # Valid column mappings that include numeric characters
        # This test validates the fix for the regex pattern that now accepts numeric characters
        # Previous regex was `re.compile(r"^\$\{(target|data)\.[a-zA-Z_]+\}$")`
        # New regex is `re.compile(r"^\$\{(target|data)\.[a-zA-Z0-9_]+\}$")`

        column_mappings_with_numbers = {
            "response": "${data.response123}",
            "query": "${data.query456}",
            "context": "${data.context789}",
        }  # This should not raise an exception with the updated regex for column mapping format validation
        # The test passes if no exception about "Unexpected references" is raised
        result = evaluate(
            data=evaluate_test_data_alphanumeric,
            evaluators={"g": GroundednessEvaluator(model_config=mock_model_config)},
            evaluator_config={
                "g": {
                    "column_mapping": column_mappings_with_numbers,
                }
            },
            fail_on_evaluator_errors=False,
        )

        # Verify that the test completed without errors related to column mapping format
        # The test data has the fields with numeric characters, so it should work correctly
        assert result is not None
        # Verify we're getting data from the numerically-named fields
        row_result_df = pd.DataFrame(result["rows"])
        assert "inputs.response123" in row_result_df.columns
        assert "inputs.query456" in row_result_df.columns
        assert "inputs.context789" in row_result_df.columns

    def test_renaming_column(self):
        """Test that the columns are renamed correctly."""
        df = pd.DataFrame(
            {
                "just_column": ["just_column."],
                "presnt_generated": ["Is present in data set."],
                "__outputs.presnt_generated": ["This was generated by target."],
                "__outputs.generated": ["Generaged by target"],
                "outputs.before": ["Despite prefix this column was before target."],
            }
        )
        df_expected = pd.DataFrame(
            {
                "inputs.just_column": ["just_column."],
                "inputs.presnt_generated": ["Is present in data set."],
                "outputs.presnt_generated": ["This was generated by target."],
                "outputs.generated": ["Generaged by target"],
                "inputs.outputs.before": ["Despite prefix this column was before target."],
            }
        )
        df_actuals = _rename_columns_conditionally(df)
        assert_frame_equal(df_actuals.sort_index(axis=1), df_expected.sort_index(axis=1))

    def test_evaluate_output_dir_not_exist(self, mock_model_config, questions_file):
        with pytest.raises(EvaluationException) as exc_info:
            evaluate(
                data=questions_file,
                evaluators={"g": GroundednessEvaluator(model_config=mock_model_config)},
                output_path="./not_exist_dir/output.jsonl",
            )

        assert "The output directory './not_exist_dir' does not exist." in exc_info.value.args[0]

    @pytest.mark.parametrize("use_relative_path", [True, False])
    def test_evaluate_output_path(self, evaluate_test_data_jsonl_file, tmpdir, use_relative_path):
        # output_path is a file
        if use_relative_path:
            output_path = os.path.join(tmpdir, "eval_test_results.jsonl")
        else:
            output_path = "eval_test_results.jsonl"

        result = evaluate(
            data=evaluate_test_data_jsonl_file,
            evaluators={"g": F1ScoreEvaluator()},
            output_path=output_path,
        )

        assert result is not None
        assert os.path.exists(output_path)
        assert os.path.isfile(output_path)

        with open(output_path, "r") as f:
            content = f.read()
            data_from_file = json.loads(content)
            assert result["metrics"] == data_from_file["metrics"]

        os.remove(output_path)

        # output_path is a directory
        result = evaluate(
            data=evaluate_test_data_jsonl_file,
            evaluators={"g": F1ScoreEvaluator()},
            output_path=os.path.join(tmpdir),
        )

        with open(os.path.join(tmpdir, DEFAULT_EVALUATION_RESULTS_FILE_NAME), "r") as f:
            content = f.read()
            data_from_file = json.loads(content)
            assert result["metrics"] == data_from_file["metrics"]

    def test_evaluate_with_errors(self):
        """Test evaluate_handle_errors"""
        data = _get_file("yeti_questions.jsonl")
        result = evaluate(data=data, evaluators={"yeti": _yeti_evaluator})
        result_df = pd.DataFrame(result["rows"])
        expected = pd.read_json(data, lines=True)
        expected.rename(columns={"query": "inputs.query", "response": "inputs.response"}, inplace=True)

        expected["outputs.yeti.result"] = expected["inputs.response"].str.len()
        expected.at[0, "outputs.yeti.result"] = math.nan
        expected.at[2, "outputs.yeti.result"] = math.nan
        expected.at[3, "outputs.yeti.result"] = math.nan
        assert_frame_equal(expected, result_df)

    @patch("azure.ai.evaluation._evaluate._evaluate._evaluate")
    def test_evaluate_main_entry_guard(self, mock_evaluate, evaluate_test_data_jsonl_file):
        err_msg = (
            "An attempt has been made to start a new process before the\n        "
            "current process has finished its bootstrapping phase."
        )
        mock_evaluate.side_effect = RuntimeError(err_msg)

        with pytest.raises(EvaluationException) as exc_info:
            evaluate(
                data=evaluate_test_data_jsonl_file,
                evaluators={"f1_score": F1ScoreEvaluator()},
            )

        assert "Please ensure the evaluate API is properly guarded with the '__main__' block" in exc_info.value.args[0]

    def test_get_trace_destination(self, mock_validate_trace_destination, mock_project_scope):
        pf_client = PFClient()
        trace_destination_without_override = pf_client._config.get_trace_destination()

        pf_client = PFClient(
            config={
                "trace.destination": (
                    _trace_destination_from_project_scope(mock_project_scope) if mock_project_scope else None
                )
            }
        )

        trace_destination_with_override = pf_client._config.get_trace_destination()

        assert trace_destination_with_override != trace_destination_without_override
        assert trace_destination_with_override == _trace_destination_from_project_scope(mock_project_scope)

    def test_content_safety_aggregation(self):
        data = {
            # 10 zeroes in a list fully written out
            "content_safety.violence_score": [0, 0, 1, 2, 5, 5, 6, 7, np.nan, None],
            "content_safety.sexual_score": [0, 0, 2, 3, 3, 3, 8, 8, np.nan, None],
            "content_safety.self_harm_score": [0, 0, 0, 0, 1, 1, 1, 1, np.nan, None],
            "content_safety.hate_unfairness_score": [0, 0, 1, 1, 2, 2, 3, 5, 6, 7],
            "content_safety.violence": [
                "low",
                "low",
                "low",
                "low",
                "high",
                "high",
                "high",
                "high",
                "high",
                "high",
            ],  # TODO DETERMINE ACTUAL BASED ON SCORES
            "content_safety.sexual": ["low", "low", "low", "low", "low", "low", "high", "high", "high", "high"],
            "content_safety.self_harm": ["low", "low", "low", "low", "low", "low", "low", "low", "high", "high"],
            "content_safety.hate_unfairness": ["low", "low", "low", "low", "low", "low", "low", "low", "low", "high"],
            "content_safety.violence_reason": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
            "content_safety.sexual_reason": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
            "content_safety.self_harm_reason": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
            "content_safety.hate_unfairness_reason": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
        }
        data_df = pd.DataFrame(data)
        evaluators = {
            "content_safety": ContentSafetyEvaluator,
        }
        aggregation = _aggregate_metrics(data_df, evaluators)

        assert len(aggregation) == 4
        assert aggregation["content_safety.violence_defect_rate"] == 0.5
        assert aggregation["content_safety.sexual_defect_rate"] == 0.25
        assert aggregation["content_safety.self_harm_defect_rate"] == 0.0
        assert aggregation["content_safety.hate_unfairness_defect_rate"] == 0.3

        no_results = _aggregate_metrics(pd.DataFrame({"content_safety.violence_score": [np.nan, None]}), evaluators)
        assert len(no_results) == 0

    def test_label_based_aggregation(self):
        data = {
            "eci.eci_label": [True, True, True, np.nan, None],
            "eci.eci_reasoning": ["a", "b", "c", "d", "e"],
            "protected_material.protected_material_label": [False, False, False, False, True],
            "protected_material.protected_material_reasoning": ["f", "g", "h", "i", "j"],
            "unknown.unaccounted_label": [False, False, False, True, True],
            "unknown.unaccounted_reasoning": ["k", "l", "m", "n", "o"],
        }
        data_df = pd.DataFrame(data)
        evaluators = {
            "eci": ECIEvaluator,
            "protected_material": ProtectedMaterialEvaluator,
        }
        aggregation = _aggregate_metrics(data_df, evaluators)
        # ECI and PM labels should be replaced with defect rates, unaccounted should not
        assert len(aggregation) == 3
        assert "eci.eci_label" not in aggregation
        assert "protected_material.protected_material_label" not in aggregation
        assert aggregation["unknown.unaccounted_label"] == 0.4

        assert aggregation["eci.eci_defect_rate"] == 1.0
        assert aggregation["protected_material.protected_material_defect_rate"] == 0.2
        assert "unaccounted_defect_rate" not in aggregation

        no_results = _aggregate_metrics(pd.DataFrame({"eci.eci_label": [np.nan, None]}), evaluators)
        assert len(no_results) == 0

    def test_other_aggregation(self):
        data = {
            "thing.groundedness_pro_label": [True, False, True, False, np.nan, None],
        }
        data_df = pd.DataFrame(data)
        evaluators = {}
        aggregation = _aggregate_metrics(data_df, evaluators)

        assert len(aggregation) == 1
        assert aggregation["thing.groundedness_pro_passing_rate"] == 0.5

        no_results = _aggregate_metrics(pd.DataFrame({"thing.groundedness_pro_label": [np.nan, None]}), {})
        assert len(no_results) == 0

    def test_general_aggregation(self):
        data = {
            "thing.metric": [1, 2, 3, 4, 5, np.nan, None],
            "thing.reasoning": ["a", "b", "c", "d", "e", "f", "g"],
            "other_thing.other_meteric": [-1, -2, -3, -4, -5, np.nan, None],
            "other_thing.other_reasoning": ["f", "g", "h", "i", "j", "i", "j"],
            "final_thing.final_metric": [False, False, False, True, True, True, False],
            "bad_thing.mixed_metric": [0, 1, False, True, 0.5, True, False],
            "bad_thing.boolean_with_nan": [True, False, True, False, True, False, np.nan],
            "bad_thing.boolean_with_none": [True, False, True, False, True, False, None],
        }
        data_df = pd.DataFrame(data)
        evaluators = {}
        aggregation = _aggregate_metrics(data_df, evaluators)

        assert len(aggregation) == 3
        assert aggregation["thing.metric"] == 3
        assert aggregation["other_thing.other_meteric"] == -3
        assert aggregation["final_thing.final_metric"] == 3 / 7.0
        assert "bad_thing.mixed_metric" not in aggregation
        assert "bad_thing.boolean_with_nan" not in aggregation
        assert "bad_thing.boolean_with_none" not in aggregation

    @pytest.mark.skip(reason="Breaking CI by crashing pytest somehow")
    def test_optional_inputs_with_data(self, questions_file, questions_answers_basic_file):
        from test_evaluators.test_inputs_evaluators import HalfOptionalEval, NoInputEval, NonOptionalEval, OptionalEval

        # All variants work with both keyworded inputs
        results = evaluate(
            data=questions_answers_basic_file,
            evaluators={
                "non": NonOptionalEval(),
                "half": HalfOptionalEval(),
                "opt": OptionalEval(),
                "no": NoInputEval(),
            },
            _use_pf_client=False,
            _use_run_submitter_client=False,
        )  # type: ignore

        first_row = results["rows"][0]
        assert first_row["outputs.non.non_score"] == 0
        assert first_row["outputs.half.half_score"] == 1
        assert first_row["outputs.opt.opt_score"] == 3

        # Variant with no default inputs fails on single input
        with pytest.raises(EvaluationException) as exc_info:
            evaluate(
                data=questions_file,
                evaluators={
                    "non": NonOptionalEval(),
                },
                _use_pf_client=False,
                _use_run_submitter_client=False,
            )  # type: ignore

        expected_message = "Some evaluators are missing required inputs:\n" "- non: ['response']\n"
        assert expected_message in exc_info.value.args[0]

        # Variants with default answer work when only question is inputted
        only_question_results = evaluate(
            data=questions_file,
            evaluators={"half": HalfOptionalEval(), "opt": OptionalEval(), "no": NoInputEval()},
            _use_pf_client=False,
            _use_run_submitter_client=False,
        )  # type: ignore

        first_row_2 = only_question_results["rows"][0]
        assert first_row_2["outputs.half.half_score"] == 0
        assert first_row_2["outputs.opt.opt_score"] == 1

    @pytest.mark.skip(reason="Breaking CI by crashing pytest somehow")
    def test_optional_inputs_with_target(self, questions_file, questions_answers_basic_file):
        from test_evaluators.test_inputs_evaluators import EchoEval

        # Check that target overrides default inputs
        target_answer_results = evaluate(
            data=questions_file,
            target=_new_answer_target,
            evaluators={"echo": EchoEval()},
            _use_pf_client=False,
            _use_run_submitter_client=False,
        )  # type: ignore

        assert target_answer_results["rows"][0]["outputs.echo.echo_query"] == "How long is flight from Earth to LV-426?"
        assert target_answer_results["rows"][0]["outputs.echo.echo_response"] == "new response"

        # Check that target replaces inputs from data (I.E. if both data and target have same output
        # the target output is sent to the evaluator.)
        question_override_results = evaluate(
            data=questions_answers_basic_file,
            target=_question_override_target,
            evaluators={"echo": EchoEval()},
            _use_pf_client=False,
            _use_run_submitter_client=False,
        )  # type: ignore

        assert question_override_results["rows"][0]["outputs.echo.echo_query"] == "new query"
        assert question_override_results["rows"][0]["outputs.echo.echo_response"] == "There is nothing good there."

        # Check that target can replace default and data inputs at the same time.
        double_override_results = evaluate(
            data=questions_answers_basic_file,
            target=_question_answer_override_target,
            evaluators={"echo": EchoEval()},
            _use_pf_client=False,
            _use_run_submitter_client=False,
        )  # type: ignore
        assert double_override_results["rows"][0]["outputs.echo.echo_query"] == "new query"
        assert double_override_results["rows"][0]["outputs.echo.echo_response"] == "new response"

    def test_conversation_aggregation_types(self, evaluate_test_data_conversion_jsonl_file):
        from test_evaluators.test_inputs_evaluators import CountingEval

        counting_eval = CountingEval()
        evaluators = {"count": counting_eval}
        # test default behavior - mean
        results = evaluate(data=evaluate_test_data_conversion_jsonl_file, evaluators=evaluators)
        assert results["rows"][0]["outputs.count.response"] == 1.5  # average of 1 and 2
        assert results["rows"][1]["outputs.count.response"] == 3.5  # average of 3 and 4

        # test maxing
        counting_eval.reset()
        counting_eval._set_conversation_aggregation_type(_AggregationType.MAX)
        results = evaluate(data=evaluate_test_data_conversion_jsonl_file, evaluators=evaluators)
        assert results["rows"][0]["outputs.count.response"] == 2
        assert results["rows"][1]["outputs.count.response"] == 4

        # test minimizing
        counting_eval.reset()
        counting_eval._set_conversation_aggregation_type(_AggregationType.MIN)
        results = evaluate(data=evaluate_test_data_conversion_jsonl_file, evaluators=evaluators)
        assert results["rows"][0]["outputs.count.response"] == 1
        assert results["rows"][1]["outputs.count.response"] == 3

        # test sum
        counting_eval.reset()
        counting_eval._set_conversation_aggregation_type(_AggregationType.SUM)
        results = evaluate(data=evaluate_test_data_conversion_jsonl_file, evaluators=evaluators)
        assert results["rows"][0]["outputs.count.response"] == 3
        assert results["rows"][1]["outputs.count.response"] == 7

        # test custom aggregator
        def custom_aggregator(values):
            return sum(values) + 1

        counting_eval.reset()
        counting_eval._set_conversation_aggregator(custom_aggregator)
        results = evaluate(data=evaluate_test_data_conversion_jsonl_file, evaluators=evaluators)
        assert results["rows"][0]["outputs.count.response"] == 4
        assert results["rows"][1]["outputs.count.response"] == 8

    def test_default_conversation_aggregation_overrides(self):
        fake_project = {"subscription_id": "123", "resource_group_name": "123", "project_name": "123"}
        eval1 = ViolenceEvaluator(None, fake_project)
        eval2 = SexualEvaluator(None, fake_project)
        eval3 = SelfHarmEvaluator(None, fake_project)
        eval4 = HateUnfairnessEvaluator(None, fake_project)
        eval5 = F1ScoreEvaluator()  # Test default
        assert eval1._conversation_aggregation_function == max
        assert eval2._conversation_aggregation_function == max
        assert eval3._conversation_aggregation_function == max
        assert eval4._conversation_aggregation_function == max
        assert eval5._conversation_aggregation_function == list_mean

    def test_conversation_aggregation_type_returns(self):
        fake_project = {"subscription_id": "123", "resource_group_name": "123", "project_name": "123"}
        eval1 = ViolenceEvaluator(None, fake_project)
        # Test builtins
        assert eval1._get_conversation_aggregator_type() == _AggregationType.MAX
        eval1._set_conversation_aggregation_type(_AggregationType.SUM)
        assert eval1._get_conversation_aggregator_type() == _AggregationType.SUM
        eval1._set_conversation_aggregation_type(_AggregationType.MAX)
        assert eval1._get_conversation_aggregator_type() == _AggregationType.MAX
        eval1._set_conversation_aggregation_type(_AggregationType.MIN)
        assert eval1._get_conversation_aggregator_type() == _AggregationType.MIN

        # test custom
        def custom_aggregator(values):
            return sum(values) + 1

        eval1._set_conversation_aggregator(custom_aggregator)
        assert eval1._get_conversation_aggregator_type() == _AggregationType.CUSTOM

    @pytest.mark.parametrize("use_async", ["true", "false"])  # Strings intended
    @pytest.mark.usefixtures("restore_env_vars")
    def test_aggregation_serialization(self, evaluate_test_data_conversion_jsonl_file, use_async):
        # This test exists to ensure that PF doesn't crash when trying to serialize a
        # complex aggregation function.
        from test_evaluators.test_inputs_evaluators import CountingEval

        counting_eval = CountingEval()
        evaluators = {"count": counting_eval}

        def custom_aggregator(values: List[float]) -> float:
            return sum(values) + 1

        os.environ["AI_EVALS_BATCH_USE_ASYNC"] = use_async
        _ = evaluate(data=evaluate_test_data_conversion_jsonl_file, evaluators=evaluators, _use_pf_client=True)
        counting_eval._set_conversation_aggregation_type(_AggregationType.MIN)
        _ = evaluate(data=evaluate_test_data_conversion_jsonl_file, evaluators=evaluators, _use_pf_client=True)
        counting_eval._set_conversation_aggregation_type(_AggregationType.SUM)
        _ = evaluate(data=evaluate_test_data_conversion_jsonl_file, evaluators=evaluators, _use_pf_client=True)
        counting_eval._set_conversation_aggregation_type(_AggregationType.MAX)
        _ = evaluate(data=evaluate_test_data_conversion_jsonl_file, evaluators=evaluators, _use_pf_client=True)
        if use_async == "true":
            counting_eval._set_conversation_aggregator(custom_aggregator)
            _ = evaluate(data=evaluate_test_data_conversion_jsonl_file, evaluators=evaluators, _use_pf_client=True)
        else:
            with pytest.raises(EvaluationException) as exc_info:
                counting_eval._set_conversation_aggregator(custom_aggregator)
                _ = evaluate(data=evaluate_test_data_conversion_jsonl_file, evaluators=evaluators, _use_pf_client=True)
            assert "TestEvaluate.test_aggregation_serialization.<locals>.custom_aggregator" in exc_info.value.args[0]

    def test_unsupported_file_inputs(self, mock_model_config, unsupported_file_type):
        with pytest.raises(EvaluationException) as cm:
            evaluate(
                data=unsupported_file_type,
                evaluators={"groundedness": GroundednessEvaluator(model_config=mock_model_config)},
            )
        assert "Unable to load data from " in cm.value.args[0]
        assert "Supported formats are JSONL and CSV. Detailed error:" in cm.value.args[0]

    def test_malformed_file_inputs(self, model_config, missing_header_csv_file, missing_columns_jsonl_file):
        with pytest.raises(EvaluationException) as exc_info:
            evaluate(
                data=missing_columns_jsonl_file,
                evaluators={"similarity": SimilarityEvaluator(model_config=model_config)},
                fail_on_evaluator_errors=True,
            )

        assert "Either 'conversation' or individual inputs must be provided." in str(exc_info.value)

        with pytest.raises(EvaluationException) as exc_info:
            evaluate(
                data=missing_header_csv_file,
                evaluators={"similarity": SimilarityEvaluator(model_config=model_config)},
                fail_on_evaluator_errors=True,
            )

        assert "Either 'conversation' or individual inputs must be provided." in str(exc_info.value)

    def test_target_failure_error_message(self, questions_file):
        with pytest.raises(EvaluationException) as exc_info:
            evaluate(
                data=questions_file,
                evaluators={"f1_score": F1ScoreEvaluator()},
                target=_target_that_fails,
            )

        assert "Evaluation target failed to produce any results. Please check the logs at " in str(exc_info.value)

    def test_evaluate_korean_characters_result(self, questions_answers_korean_file):
        output_path = "eval_test_results_korean.jsonl"

        result = evaluate(
            data=questions_answers_korean_file,
            evaluators={"g": F1ScoreEvaluator()},
            output_path=output_path,
        )

        assert result is not None

        with open(questions_answers_korean_file, "r", encoding="utf-8") as f:
            first_line = f.readline()
            data_from_file = json.loads(first_line)

        assert result["rows"][0]["inputs.query"] == data_from_file["query"]

        os.remove(output_path)

    def test_name_map_conversion(self):
        test_map = {
            "name1": "property1",
            "name2": "property2",
            "name3": "property3",
        }
        map_dump = json.dumps(test_map)

        # Test basic
        result = _convert_name_map_into_property_entries(test_map)
        assert result[EvaluationRunProperties.NAME_MAP_LENGTH] == 1
        assert result[f"{EvaluationRunProperties.NAME_MAP}_0"] == map_dump

        # Test with splits (dump of test map is 66 characters long)
        result = _convert_name_map_into_property_entries(test_map, segment_length=40)
        assert result[EvaluationRunProperties.NAME_MAP_LENGTH] == 2
        combined_strings = (
            result[f"{EvaluationRunProperties.NAME_MAP}_0"] + result[f"{EvaluationRunProperties.NAME_MAP}_1"]
        )
        # breakpoint()
        assert result[f"{EvaluationRunProperties.NAME_MAP}_0"] == map_dump[0:40]
        assert result[f"{EvaluationRunProperties.NAME_MAP}_1"] == map_dump[40:]
        assert combined_strings == map_dump

        # Test with exact split
        result = _convert_name_map_into_property_entries(test_map, segment_length=22)
        assert result[EvaluationRunProperties.NAME_MAP_LENGTH] == 3
        combined_strings = (
            result[f"{EvaluationRunProperties.NAME_MAP}_0"]
            + result[f"{EvaluationRunProperties.NAME_MAP}_1"]
            + result[f"{EvaluationRunProperties.NAME_MAP}_2"]
        )
        assert result[f"{EvaluationRunProperties.NAME_MAP}_0"] == map_dump[0:22]
        assert result[f"{EvaluationRunProperties.NAME_MAP}_1"] == map_dump[22:44]
        assert result[f"{EvaluationRunProperties.NAME_MAP}_2"] == map_dump[44:]
        assert combined_strings == map_dump

        # Test failure case
        result = _convert_name_map_into_property_entries(test_map, segment_length=10, max_segments=1)
        assert result[EvaluationRunProperties.NAME_MAP_LENGTH] == -1
        assert len(result) == 1
