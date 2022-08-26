from enum import Enum


__all__ = ["SchemaType", "PropertyFormat", "ContentType", "InParameterChoice"]


class SchemaType(Enum):
    integer = "integer"
    string = "string"
    object = "object"
    array = "array"
    number = "numbers"


class PropertyFormat(Enum):
    dateTime = "date-time"


class ContentType(Enum):
    any = "*/*"
    json = "application/json"
    html = "text/html"


class InParameterChoice(Enum):
    query = "query"
    header = "header"
    path = "path"
    cookie = "cookie"
