import typing as t

from dataclasses import dataclass
from enum import Enum


__all__ = ["Schema", "SchemaType", "PropertyFormat"]


class SchemaType(Enum):
    integer = "integer"
    string = "string"
    object = "object"
    array = "array"
    number = "numbers"


class PropertyFormat(Enum):
    dateTime = "date-time"


@dataclass
class Schema:
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#schemaObject
    """

    type: SchemaType
    properties: t.Optional[dict[str, "Schema"]] = None
    items: t.Optional["Schema"] = None
    required: t.Optional[list[str]] = None
    readOnly: t.Optional[bool] = None
    writeOnly: t.Optional[bool] = None
    nullable: bool | None = None
    minimum: int | None = None
    format: PropertyFormat | None = None
    enum: t.Optional[t.Sequence[str]] = None
    description: t.Optional[str] = None

    def __post_init__(self):
        if self.type == SchemaType.object:
            self._validate_object()

    def _validate_object(self):
        if self.properties is None:
            raise ValueError(
                f"""Schema {self} is of type "object" should define `properties`"""
            )
        set_of_properties = {prop_name for prop_name in self.properties.keys()}
        set_of_required = set(self.required)

        unknown = set_of_required - set_of_properties
        if unknown:
            raise ValueError(
                f"These properties {unknown} are required, but are missing in property list in schema: {self}"
            )
