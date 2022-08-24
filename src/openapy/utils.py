import json
import typing as t
from enum import Enum


def remove_nulls(obj: t.Any) -> None:
    """
    Recursively traverses through a dict and its sub-structures and
    removes all keys whose value is None.

    Makes all changes in-place.
    """
    if isinstance(obj, list):
        for item in obj:
            remove_nulls(item)
    elif isinstance(obj, dict):
        for key, value in tuple(obj.items()):
            if value is None:
                del obj[key]
                continue
            elif isinstance(key, Enum):
                obj[key.value] = obj.pop(key)
            elif isinstance(key, str) and key.endswith("__"):
                obj[key.strip("_")] = obj.pop(key)

            remove_nulls(value)


class Encoder(json.JSONEncoder):
    """
    Custom encoder class for json.dumps to correctly serialize
    enum.Enum choice values
    """

    def default(self, o):
        if isinstance(o, Enum):
            return o.value
        super().default(o)
