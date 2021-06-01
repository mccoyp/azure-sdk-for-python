# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import pytest
from enum import Enum
import json
import isodate
from datetime import date, timedelta, time, datetime
from azure.core.serialization import ComplexEncoder, NULL


def _expand_value(obj):
    try:
        try:
            return obj.to_dict()

        except AttributeError:
            if isinstance(obj, Enum):
                return obj.value
            elif isinstance(obj, list):
                return [_expand_value(item) for item in obj]
            elif isinstance(obj, dict):
                return _expand_dict(obj)
            else:
                return _expand_dict(vars(obj))

    except TypeError:
        return obj


def _expand_dict(d):
    return dict((key, _expand_value(value)) for key, value in d.items())


class SerializerMixin(object):
    """Mixin that provides methods for representing a model as a dictionary"""

    def to_dict(self):
        return _expand_value(vars(self))


def test_NULL_is_falsy():
    assert NULL is not False
    assert bool(NULL) is False
    assert NULL is NULL

@pytest.fixture
def json_dumps_with_encoder():
    def func(obj):
        return json.dumps(obj, cls=ComplexEncoder)
    return func

def test_dictionary_basic(json_dumps_with_encoder):
    test_obj = {
        "string": "myid",
        "number": 42,
        "boolean": True,
        "list_of_string": [1, 2, 3],
        "dictionary_of_number": {"pi": 3.14},
    }
    complex_serialized = json_dumps_with_encoder(test_obj)
    assert json.dumps(test_obj) == complex_serialized
    assert json.loads(complex_serialized) == test_obj

def test_model_basic(json_dumps_with_encoder):
    class BasicModel(SerializerMixin):
        def __init__(self):
            self.string = "myid"
            self.number = 42
            self.boolean = True
            self.list_of_string = [1, 2, 3]
            self.dictionary_of_number = {"pi": 3.14}

    def assert_basic_models_equal(test_obj, expected):
        assert test_obj.string == expected.string
        assert test_obj.number == expected.number
        assert test_obj.boolean == expected.boolean
        assert test_obj.list_of_string == expected.list_of_string
        assert expected.dictionary_of_number == expected.dictionary_of_number

    expected = BasicModel()
    test_obj = BasicModel.from_dict(expected.to_dict())
    assert_basic_models_equal(test_obj, expected)

    expected_dict = {
        "string": "myid",
        "number": 42,
        "boolean": True,
        "list_of_string": [1, 2, 3],
        "dictionary_of_number": {"pi": 3.14},
    }
    assert json.loads(json_dumps_with_encoder(test_obj)) == expected_dict

def test_dictionary_datetime(json_dumps_with_encoder):
    test_obj = {
        "timedelta": timedelta(1),
        "date": date(2021, 5, 12),
        "datetime": isodate.parse_datetime('2012-02-24T00:53:52.780Z'),
        "time": time(11,12,13),
    }
    expected = {
        "timedelta": "P1D",
        "date": "2021-05-12",
        "datetime": '2012-02-24T00:53:52.780Z',
        'time': '11:12:13',
    }
    assert json.loads(json_dumps_with_encoder(test_obj)) == expected

def test_model_datetime(json_dumps_with_encoder):
    class DatetimeModel(SerializerMixin):
        def __init__(self):
            self.timedelta = timedelta(1)
            self.date = date(2021, 5, 12)
            self.datetime = isodate.parse_datetime('2012-02-24T00:53:52.780Z')
            self.time = time(11,12,13)

    def assert_datetime_models_equal(test_obj, expected):
        assert test_obj.timedelta == expected.timedelta
        assert test_obj.date == expected.date
        assert test_obj.datetime == expected.datetime
        assert test_obj.time == expected.time

    expected = DatetimeModel()

    test_obj = DatetimeModel.from_dict(expected.to_dict())
    assert_datetime_models_equal(test_obj, expected)

    expected_dict = {
        "timedelta": "P1D",
        "date": "2021-05-12",
        "datetime": '2012-02-24T00:53:52.780Z',
        'time': '11:12:13',
    }
    assert json.loads(json_dumps_with_encoder(test_obj)) == expected_dict

def test_serialize_datetime(json_dumps_with_encoder):

    date_obj = isodate.parse_datetime('2015-01-01T00:00:00')
    date_str = json_dumps_with_encoder(date_obj)

    assert date_str == '"2015-01-01T00:00:00.000Z"'

    date_obj = isodate.parse_datetime('1999-12-31T23:59:59-12:00')
    date_str = json_dumps_with_encoder(date_obj)

    assert date_str == '"2000-01-01T11:59:59.000Z"'

    date_obj = isodate.parse_datetime("2015-06-01T16:10:08.0121-07:00")
    date_str = json_dumps_with_encoder(date_obj)

    assert date_str == '"2015-06-01T23:10:08.0121Z"'

    date_obj = datetime.min
    date_str = json_dumps_with_encoder(date_obj)
    assert date_str == '"0001-01-01T00:00:00.000Z"'

    date_obj = datetime.max
    date_str = json_dumps_with_encoder(date_obj)
    assert date_str == '"9999-12-31T23:59:59.999999Z"'

    date_obj = isodate.parse_datetime('2012-02-24T00:53:52.000001Z')
    date_str = json_dumps_with_encoder(date_obj)
    assert date_str == '"2012-02-24T00:53:52.000001Z"'

    date_obj = isodate.parse_datetime('2012-02-24T00:53:52.780Z')
    date_str = json_dumps_with_encoder(date_obj)
    assert date_str == '"2012-02-24T00:53:52.780Z"'

def test_serialize_time(json_dumps_with_encoder):

    time_str = json_dumps_with_encoder(time(11,22,33))
    assert time_str == '"11:22:33"'

    time_str = json_dumps_with_encoder(time(11,22,33,444444))
    assert time_str == '"11:22:33.444444"'

class BasicEnum(Enum):
    val = "Basic"

class StringEnum(str, Enum):
    val = "string"

class IntEnum(int, Enum):
    val = 1

class FloatEnum(float, Enum):
    val = 1.5

def test_dictionary_enum(json_dumps_with_encoder):
    test_obj = {
        "basic": BasicEnum.val
    }
    with pytest.raises(TypeError):
        json_dumps_with_encoder(test_obj)

    test_obj = {
        "basic": BasicEnum.val.value,
        "string": StringEnum.val,
        "int": IntEnum.val,
        "float": FloatEnum.val
    }
    expected = {
        "basic": "Basic",
        "string": "string",
        "int": 1,
        "float": 1.5
    }
    serialized = json_dumps_with_encoder(test_obj)
    assert json.dumps(test_obj) == serialized
    assert json.loads(serialized) == expected

def test_model_enum(json_dumps_with_encoder):
    class BasicEnumModel:
        def __init__(self):
            self.basic = BasicEnum.val

    with pytest.raises(TypeError):
        json_dumps_with_encoder(BasicEnumModel())

    class EnumModel(SerializerMixin):
        def __init__(self):
            self.basic = BasicEnum.val.value
            self.string = StringEnum.val
            self.int = IntEnum.val
            self.float = FloatEnum.val

    def assert_enum_models_equal(test_obj, expected):
        assert test_obj.basic == expected.basic
        assert test_obj.string == expected.string
        assert test_obj.int == expected.int
        assert test_obj.float == expected.float

    expected = EnumModel()
    test_obj = EnumModel.from_dict(expected.to_dict())
    assert_enum_models_equal(test_obj, expected)

    expected_dict = {
        "basic": "Basic",
        "string": "string",
        "int": 1,
        "float": 1.5
    }
    assert json.loads(json_dumps_with_encoder(test_obj)) == expected_dict

def test_dictionary_none(json_dumps_with_encoder):
    assert json_dumps_with_encoder(None) == json.dumps(None)
    test_obj = {
        "entry": None
    }
    assert json.loads(json_dumps_with_encoder(test_obj)) == test_obj

def test_model_none(json_dumps_with_encoder):
    class NoneModel(SerializerMixin):
        def __init__(self):
            self.entry = None

    expected = NoneModel()
    test_obj = NoneModel.from_dict(expected.to_dict())
    assert expected.entry == test_obj.entry
    expected_dict = {"entry": None}
    assert json.loads(json_dumps_with_encoder(test_obj)) == expected_dict

def test_dictionary_empty_collections(json_dumps_with_encoder):
    test_obj = {
        "dictionary": {},
        "list": [],
        # "tuple": (), json represents tuples as lists, so this won't round-trip with json.loads
        # "set": set(), json can't serialize sets. should we?
    }

    assert json.dumps(test_obj) == json_dumps_with_encoder(test_obj)
    assert json.loads(json_dumps_with_encoder(test_obj)) == test_obj

def test_model_empty_collections(json_dumps_with_encoder):
    class EmptyCollectionsModel(SerializerMixin):
        def __init__(self):
            self.dictionary = {}
            self.list = []
            self.tuple = ()
            # self.set = set() json can't serialize sets. should we?

    def assert_empty_collections_models_equal(test_obj, expected):
        assert test_obj.dictionary == expected.dictionary
        assert test_obj.list == expected.list
        assert test_obj.tuple == expected.tuple

    expected = EmptyCollectionsModel()
    test_obj = EmptyCollectionsModel.from_dict(expected.to_dict())
    assert_empty_collections_models_equal(expected, test_obj)
    expected_dict = {
        "dictionary": {},
        "list": [],
        "tuple": (),
    }
    assert json.loads(json_dumps_with_encoder(test_obj)) == expected_dict

def test_model_inheritance(json_dumps_with_encoder):
    class ParentModel(SerializerMixin):
        def __init__(self):
            self.parent = "parent"

    class ChildModel(ParentModel):
        def __init__(self):
            super(ChildModel, self).__init__()
            self.child = "child"

    def assert_child_models_equal(test_obj, expected):
        assert test_obj.parent == expected.parent
        assert test_obj.child == expected.child

    expected = ChildModel()
    test_obj = ChildModel.from_dict(expected.to_dict())
    assert_child_models_equal(test_obj, expected)
    expected_dict = {
        "parent": "parent",
        "child": "child",
    }
    assert json.loads(json_dumps_with_encoder(test_obj)) == expected_dict

def test_model_recursion(json_dumps_with_encoder):
    class RecursiveModel(SerializerMixin):
        def __init__(self):
            self.name = "it's me!"
            self.list_of_me = None
            self.dict_of_me = None
            self.dict_of_list_of_me = None
            self.list_of_dict_of_me = None

    def assert_recursive_models_equal(test_obj, expected):
        assert test_obj.name == expected.name
        assert test_obj.list_of_me == expected.list_of_me
        assert test_obj.dict_of_me == expected.dict_of_me
        assert test_obj.dict_of_list_of_me == expected.dict_of_list_of_me
        assert test_obj.list_of_dict_of_me == expected.list_of_dict_of_me

    expected = RecursiveModel()
    expected.list_of_me = [RecursiveModel()]
    expected.dict_of_me = {"me": RecursiveModel()}
    expected.dict_of_list_of_me = {"many mes": [RecursiveModel()]}
    expected.list_of_dict_of_me = [{"me": RecursiveModel()}]

    test_obj = RecursiveModel.from_dict(expected.to_dict())
    assert_recursive_models_equal(test_obj, expected)
    expected_dict = {
        "name": "it's me!",
        "list_of_me": [{"name": "it's me!"}],
        "dict_of_me": {"me": {"name": "it's me!"}},
        "dict_of_list_of_me": {"many mes": [{"name": "it's me!"}]},
        "list_of_dict_of_me": [{"me": {"name": "it's me!"}}]
    }
    assert json.loads(json_dumps_with_encoder(test_obj)) == expected_dict
