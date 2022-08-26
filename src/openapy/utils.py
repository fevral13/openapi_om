import json
import typing as t
from dataclasses import asdict, dataclass
from enum import Enum

import yaml


class ValidationError(Exception):
    def __init__(self, message, schema_object):
        self.schema_object = schema_object
        self.message = message

    def __str__(self):
        return f"Error in object {self.schema_object}: {self.message}"


@dataclass
class BaseNode:
    def as_dict(self) -> dict[str, t.Any]:
        schema_dict = asdict(self)
        remove_nulls(schema_dict)
        return schema_dict

    def as_json(self, **kwargs) -> str:
        return json.dumps(self.as_dict(), cls=Encoder, **kwargs)

    def as_yaml(self) -> str:
        schema_dict = json.loads(self.as_json())
        return yaml.dump(schema_dict, explicit_start=True)


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
            elif isinstance(key, str) and key.endswith("_"):
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
