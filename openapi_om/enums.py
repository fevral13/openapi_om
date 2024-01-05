from enum import Enum


__all__ = [
    "ContentType",
    "InParameterChoice",
    "InSecuritySchemeChoice",
    "PropertyFormat",
    "SchemaType",
    "SecuritySchemeChoice",
]


class BaseEnum(Enum):
    def __repr__(self) -> str:
        return str(self)


class SchemaType(BaseEnum):
    null = "null"
    integer = "integer"
    string = "string"
    object = "object"
    array = "array"
    number = "number"
    boolean = "boolean"


class PropertyFormat(BaseEnum):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#data-types
    """

    integer = "int32"
    long = "int64"
    float = "float"
    double = "double"
    string = ""
    byte = "byte"
    binary = "binary"
    boolean = ""
    date = "date"
    """As defined by full-date - RFC3339"""

    dateTime = "date-time"
    """As defined by full-date - RFC3339"""

    password = "password"


class ContentType(BaseEnum):
    # todo:
    any = "*/*"
    json = "application/json"
    application = "application/*"
    html = "text/html"
    multipart_formdata = "multipart/form-data"
    text_csv = "text/csv"


class InParameterChoice(BaseEnum):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#parameter-locations
    """

    query = "query"
    header = "header"
    path = "path"
    cookie = "cookie"


class SecuritySchemeChoice(BaseEnum):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#fixed-fields-23
    """

    apiKey = "apiKey"
    http = "http"
    oauth2 = "oauth2"
    openIdConnect = "openIdConnect"


class InSecuritySchemeChoice(BaseEnum):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#fixed-fields-23
    """

    query = "query"
    header = "header"
    cookie = "cookie"
