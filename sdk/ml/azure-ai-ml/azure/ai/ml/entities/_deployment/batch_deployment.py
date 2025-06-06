# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=protected-access

import logging
import warnings
from os import PathLike
from pathlib import Path
from typing import Any, Dict, Optional, Union

from azure.ai.ml._restclient.v2024_01_01_preview.models import BatchDeployment as BatchDeploymentData
from azure.ai.ml._restclient.v2024_01_01_preview.models import BatchDeploymentProperties as RestBatchDeployment
from azure.ai.ml._restclient.v2024_01_01_preview.models import BatchOutputAction
from azure.ai.ml._restclient.v2024_01_01_preview.models import CodeConfiguration as RestCodeConfiguration
from azure.ai.ml._restclient.v2024_01_01_preview.models import IdAssetReference
from azure.ai.ml._schema._deployment.batch.batch_deployment import BatchDeploymentSchema
from azure.ai.ml._utils._arm_id_utils import _parse_endpoint_name_from_deployment_id
from azure.ai.ml.constants._common import BASE_PATH_CONTEXT_KEY, PARAMS_OVERRIDE_KEY
from azure.ai.ml.constants._deployment import BatchDeploymentOutputAction
from azure.ai.ml.entities._assets import Environment, Model
from azure.ai.ml.entities._deployment.deployment_settings import BatchRetrySettings
from azure.ai.ml.entities._job.resource_configuration import ResourceConfiguration
from azure.ai.ml.entities._system_data import SystemData
from azure.ai.ml.entities._util import load_from_dict
from azure.ai.ml.exceptions import ErrorCategory, ErrorTarget, ValidationErrorType, ValidationException

from .code_configuration import CodeConfiguration
from .deployment import Deployment
from .model_batch_deployment_settings import ModelBatchDeploymentSettings as BatchDeploymentSettings

module_logger = logging.getLogger(__name__)

SETTINGS_ATTRIBUTES = [
    "output_action",
    "output_file_name",
    "error_threshold",
    "retry_settings",
    "logging_level",
    "mini_batch_size",
    "max_concurrency_per_instance",
    "environment_variables",
]


class BatchDeployment(Deployment):
    """Batch endpoint deployment entity.

    **Warning** This class should not be used directly.
    Please use one of the child implementations, :class:`~azure.ai.ml.entities.ModelBatchDeployment` or
    :class:`azure.ai.ml.entities.PipelineComponentBatchDeployment`.

    :param name: the name of the batch deployment
    :type name: str
    :param description: Description of the resource.
    :type description: str
    :param tags: Tag dictionary. Tags can be added, removed, and updated.
    :type tags: dict[str, str]
    :param properties: The asset property dictionary.
    :type properties: dict[str, str]
    :param model: Model entity for the endpoint deployment, defaults to None
    :type model: Union[str, Model]
    :param code_configuration: defaults to None
    :type code_configuration: CodeConfiguration
    :param environment: Environment entity for the endpoint deployment., defaults to None
    :type environment: Union[str, Environment]
    :param compute: Compute target for batch inference operation.
    :type compute: str
    :param output_action: Indicates how the output will be organized. Possible values include:
     "summary_only", "append_row". Defaults to "append_row"
    :type output_action: str or ~azure.ai.ml.constants._deployment.BatchDeploymentOutputAction
    :param output_file_name: Customized output file name for append_row output action, defaults to "predictions.csv"
    :type output_file_name: str
    :param max_concurrency_per_instance: Indicates maximum number of parallelism per instance, defaults to 1
    :type max_concurrency_per_instance: int
    :param error_threshold: Error threshold, if the error count for the entire input goes above
        this value,
        the batch inference will be aborted. Range is [-1, int.MaxValue]
        -1 value indicates, ignore all failures during batch inference
        For FileDataset count of file failures
        For TabularDataset, this is the count of record failures, defaults to -1
    :type error_threshold: int
    :param retry_settings: Retry settings for a batch inference operation, defaults to None
    :type retry_settings: BatchRetrySettings
    :param resources: Indicates compute configuration for the job.
    :type resources: ~azure.mgmt.machinelearningservices.models.ResourceConfiguration
    :param logging_level: Logging level for batch inference operation, defaults to "info"
    :type logging_level: str
    :param mini_batch_size: Size of the mini-batch passed to each batch invocation, defaults to 10
    :type mini_batch_size: int
    :param environment_variables: Environment variables that will be set in deployment.
    :type environment_variables: dict
    :param code_path: Folder path to local code assets. Equivalent to code_configuration.code.
    :type code_path: Union[str, PathLike]
    :param scoring_script: Scoring script name. Equivalent to code_configuration.code.scoring_script.
    :type scoring_script: Union[str, PathLike]
    :param instance_count: Number of instances the interfering will run on. Equivalent to resources.instance_count.
    :type instance_count: int
    :raises ~azure.ai.ml.exceptions.ValidationException: Raised if BatchDeployment cannot be successfully validated.
        Details will be provided in the error message.
    """

    def __init__(
        self,
        *,
        name: str,
        endpoint_name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[Dict[str, Any]] = None,
        properties: Optional[Dict[str, str]] = None,
        model: Optional[Union[str, Model]] = None,
        code_configuration: Optional[CodeConfiguration] = None,
        environment: Optional[Union[str, Environment]] = None,
        compute: Optional[str] = None,
        resources: Optional[ResourceConfiguration] = None,
        output_file_name: Optional[str] = None,
        output_action: Optional[Union[BatchDeploymentOutputAction, str]] = None,
        error_threshold: Optional[int] = None,
        retry_settings: Optional[BatchRetrySettings] = None,
        logging_level: Optional[str] = None,
        mini_batch_size: Optional[int] = None,
        max_concurrency_per_instance: Optional[int] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        code_path: Optional[Union[str, PathLike]] = None,  # promoted property from code_configuration.code
        scoring_script: Optional[
            Union[str, PathLike]
        ] = None,  # promoted property from code_configuration.scoring_script
        instance_count: Optional[int] = None,  # promoted property from resources.instance_count
        **kwargs: Any,
    ) -> None:
        _type = kwargs.pop("_type", None)

        # Suppresses deprecation warning when object is created from REST responses
        # This is needed to avoid false deprecation warning on model batch deployment
        if _type is None and not kwargs.pop("_from_rest", False):
            warnings.warn(
                "This class is intended as a base class and it's direct usage is deprecated. "
                "Use one of the concrete implementations instead:\n"
                "* ModelBatchDeployment - For model-based batch deployments\n"
                "* PipelineComponentBatchDeployment - For pipeline component-based batch deployments"
            )
        self._provisioning_state: Optional[str] = kwargs.pop("provisioning_state", None)

        settings = kwargs.pop("settings", None)
        super(BatchDeployment, self).__init__(
            name=name,
            type=_type,
            endpoint_name=endpoint_name,
            properties=properties,
            tags=tags,
            description=description,
            model=model,
            code_configuration=code_configuration,
            environment=environment,
            environment_variables=environment_variables,  # needed, otherwise Deployment.__init__() will set it to {}
            code_path=code_path,
            scoring_script=scoring_script,
            **kwargs,
        )

        self.compute = compute
        self.resources = resources

        self._settings = (
            settings
            if settings
            else BatchDeploymentSettings(
                mini_batch_size=mini_batch_size,
                instance_count=instance_count,
                max_concurrency_per_instance=max_concurrency_per_instance,
                output_action=output_action,
                output_file_name=output_file_name,
                retry_settings=retry_settings,
                environment_variables=environment_variables,
                error_threshold=error_threshold,
                logging_level=logging_level,
            )
        )

        self._setup_instance_count()

    def _setup_instance_count(
        self,
    ) -> None:  # No need to check instance_count here as it's already set in self._settings during initialization
        if self.resources and self._settings.instance_count:
            msg = "Can't set instance_count when resources is provided."
            raise ValidationException(
                message=msg,
                target=ErrorTarget.BATCH_DEPLOYMENT,
                no_personal_data_message=msg,
                error_category=ErrorCategory.USER_ERROR,
                error_type=ValidationErrorType.INVALID_VALUE,
            )

        if not self.resources and self._settings.instance_count:
            self.resources = ResourceConfiguration(instance_count=self._settings.instance_count)

    def __getattr__(self, name: str) -> Optional[Any]:
        # Support backwards compatibility with old BatchDeployment properties.
        if name in SETTINGS_ATTRIBUTES:
            try:
                return getattr(self._settings, name)
            except AttributeError:
                pass
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        # Support backwards compatibility with old BatchDeployment properties.
        if name in SETTINGS_ATTRIBUTES:
            try:
                setattr(self._settings, name, value)
            except AttributeError:
                pass
        super().__setattr__(name, value)

    @property
    def instance_count(self) -> Optional[int]:
        return self.resources.instance_count if self.resources else None

    @instance_count.setter
    def instance_count(self, value: int) -> None:
        if not self.resources:
            self.resources = ResourceConfiguration()

        self.resources.instance_count = value

    @property
    def provisioning_state(self) -> Optional[str]:
        """Batch deployment provisioning state, readonly.

        :return: Batch deployment provisioning state.
        :rtype: Optional[str]
        """
        return self._provisioning_state

    def _to_dict(self) -> Dict:
        res: dict = BatchDeploymentSchema(context={BASE_PATH_CONTEXT_KEY: "./"}).dump(self)
        return res

    @classmethod
    def _rest_output_action_to_yaml_output_action(cls, rest_output_action: str) -> str:
        output_switcher = {
            BatchOutputAction.APPEND_ROW: BatchDeploymentOutputAction.APPEND_ROW,
            BatchOutputAction.SUMMARY_ONLY: BatchDeploymentOutputAction.SUMMARY_ONLY,
        }

        return output_switcher.get(rest_output_action, rest_output_action)

    @classmethod
    def _yaml_output_action_to_rest_output_action(cls, yaml_output_action: Any) -> str:
        output_switcher = {
            BatchDeploymentOutputAction.APPEND_ROW: BatchOutputAction.APPEND_ROW,
            BatchDeploymentOutputAction.SUMMARY_ONLY: BatchOutputAction.SUMMARY_ONLY,
        }

        return output_switcher.get(yaml_output_action, yaml_output_action)

    # pylint: disable=arguments-differ
    def _to_rest_object(self, location: str) -> BatchDeploymentData:  # type: ignore[override]
        self._validate()
        code_config = (
            RestCodeConfiguration(
                code_id=self.code_configuration.code,
                scoring_script=self.code_configuration.scoring_script,
            )
            if self.code_configuration
            else None
        )
        model = IdAssetReference(asset_id=self.model) if self.model else None
        environment = self.environment

        batch_deployment: RestBatchDeployment = None
        # Create base RestBatchDeployment object with common properties
        batch_deployment = RestBatchDeployment(
            compute=self.compute,
            description=self.description,
            resources=self.resources._to_rest_object() if self.resources else None,
            code_configuration=code_config,
            environment_id=environment,
            model=model,
            output_file_name=self.output_file_name,
            output_action=(
                BatchDeployment._yaml_output_action_to_rest_output_action(self.output_action)
                if isinstance(self.output_action, str)
                else None
            ),
            error_threshold=self.error_threshold,
            retry_settings=self.retry_settings._to_rest_object() if self.retry_settings else None,
            logging_level=self.logging_level,
            mini_batch_size=self.mini_batch_size,
            max_concurrency_per_instance=self.max_concurrency_per_instance,
            environment_variables=self.environment_variables,
            properties=self.properties,
        )

        return BatchDeploymentData(location=location, properties=batch_deployment, tags=self.tags)

    @classmethod
    def _from_rest_object(  # pylint: disable=arguments-renamed
        cls, deployment: BatchDeploymentData
    ) -> BatchDeploymentData:
        modelId = deployment.properties.model.asset_id if deployment.properties.model else None

        if (
            hasattr(deployment.properties, "deployment_configuration")
            and deployment.properties.deployment_configuration is not None
        ):
            settings = deployment.properties.deployment_configuration.settings
            deployment_comp_settings = {
                "deployment_configuration_type": deployment.properties.deployment_configuration.deployment_configuration_type,  # pylint: disable=line-too-long
                "componentDeployment.Settings.continue_on_step_failure": settings.get(
                    "ComponentDeployment.Settings.continue_on_step_failure", None
                ),
                "default_datastore": settings.get("default_datastore", None),
                "default_compute": settings.get("default_compute", None),
            }
            properties = {}
            if deployment.properties.properties:
                properties.update(deployment.properties.properties)
            properties.update(deployment_comp_settings)
        else:
            properties = deployment.properties.properties

        code_configuration = (
            CodeConfiguration._from_rest_code_configuration(deployment.properties.code_configuration)
            if deployment.properties.code_configuration
            else None
        )
        deployment = BatchDeployment(
            name=deployment.name,
            description=deployment.properties.description,
            id=deployment.id,
            tags=deployment.tags,
            model=modelId,
            environment=deployment.properties.environment_id,
            code_configuration=code_configuration,
            output_file_name=(
                deployment.properties.output_file_name
                if cls._rest_output_action_to_yaml_output_action(deployment.properties.output_action)
                == BatchDeploymentOutputAction.APPEND_ROW
                else None
            ),
            output_action=cls._rest_output_action_to_yaml_output_action(deployment.properties.output_action),
            error_threshold=deployment.properties.error_threshold,
            retry_settings=BatchRetrySettings._from_rest_object(deployment.properties.retry_settings),
            logging_level=deployment.properties.logging_level,
            mini_batch_size=deployment.properties.mini_batch_size,
            compute=deployment.properties.compute,
            resources=ResourceConfiguration._from_rest_object(deployment.properties.resources),
            environment_variables=deployment.properties.environment_variables,
            max_concurrency_per_instance=deployment.properties.max_concurrency_per_instance,
            endpoint_name=_parse_endpoint_name_from_deployment_id(deployment.id),
            properties=properties,
            creation_context=SystemData._from_rest_object(deployment.system_data),
            provisioning_state=deployment.properties.provisioning_state,
            _from_rest=True,
        )

        return deployment

    @classmethod
    def _load(
        cls,
        data: Optional[Dict] = None,
        yaml_path: Optional[Union[PathLike, str]] = None,
        params_override: Optional[list] = None,
        **kwargs: Any,
    ) -> "BatchDeployment":
        data = data or {}
        params_override = params_override or []
        cls._update_params(params_override)

        context = {
            BASE_PATH_CONTEXT_KEY: Path(yaml_path).parent if yaml_path else Path.cwd(),
            PARAMS_OVERRIDE_KEY: params_override,
        }
        res: BatchDeployment = load_from_dict(BatchDeploymentSchema, data, context, **kwargs)
        return res

    def _validate(self) -> None:
        self._validate_output_action()

    @classmethod
    def _update_params(cls, params_override: Any) -> None:
        for param in params_override:
            endpoint_name = param.get("endpoint_name")
            if isinstance(endpoint_name, str):
                param["endpoint_name"] = endpoint_name.lower()

    def _validate_output_action(self) -> None:
        if (
            self.output_action
            and self.output_action == BatchDeploymentOutputAction.SUMMARY_ONLY
            and self.output_file_name
        ):
            msg = "When output_action is set to {}, the output_file_name need not to be specified."
            msg = msg.format(BatchDeploymentOutputAction.SUMMARY_ONLY)
            raise ValidationException(
                message=msg,
                target=ErrorTarget.BATCH_DEPLOYMENT,
                no_personal_data_message=msg,
                error_category=ErrorCategory.USER_ERROR,
                error_type=ValidationErrorType.INVALID_VALUE,
            )
