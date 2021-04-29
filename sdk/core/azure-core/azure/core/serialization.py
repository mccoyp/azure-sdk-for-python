# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import base64
import datetime
from json import JSONEncoder

import isodate

__all__ = ["NULL"]

class _Null(object):
    """To create a Falsy object
    """
    def __bool__(self):
        return False

    __nonzero__ = __bool__ # Python2 compatibility


NULL = _Null()
"""
A falsy sentinel object which is supposed to be used to specify attributes
with no data. This gets serialized to `null` on the wire.
"""


class UTC(datetime.tzinfo):
    """Time Zone info for handling UTC"""

    def utcoffset(self, dt):
        """UTF offset for UTC is 0."""
        return datetime.timedelta(0)

    def tzname(self, dt):
        """Timestamp representation."""
        return "Z"

    def dst(self, dt):
        """No daylight saving for UTC."""
        return datetime.timedelta(hours=1)


try:
    from datetime import timezone
    TZ_UTC = timezone.utc  # type: ignore
except ImportError:
    TZ_UTC = UTC()  # type: ignore


class ComplexEncoder(JSONEncoder):
    """A JSON encoder that's capable of serializing datetime objects and bytes.
    """

    def default(self, obj):
        try:
            return super(ComplexEncoder, self).default(obj)
        except TypeError:
            obj_type = type(obj)
            if obj_type is datetime.date:
                return obj.isoformat()
            elif obj_type is datetime.datetime:
                return obj.astimezone(TZ_UTC).isoformat()
            elif obj_type is datetime.timedelta:
                return isodate.duration_isoformat(obj)
            elif obj_type is bytes or obj_type is bytearray:
                return base64.b64encode(obj).decode('utf-8')
            else:
                return super(ComplexEncoder, self).default(obj)
