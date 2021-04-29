# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from enum import Enum


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


class SerializingMixin(object):
    """Mixin that provides methods for representing a model as a dictionary"""

    def to_dict(self):
        """Returns a dictionary representation of an object that can be serialized into JSON.
        
        A JSONEncoder that supports datetime object serialization may be necessary to correctly serialize the returned
        dictionary.
        """

        return _expand_value(vars(self))
