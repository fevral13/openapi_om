import typing as t
from dataclasses import dataclass
from enum import Enum

from .schema import Schema


__all__ = [
    "Path",
    "Operation",
    "Response",
    "MediaType",
    "ContentType",
    "Encoding",
    "Parameter",
    "InParameterChoice",
    "RequestBody",
]


class ContentType(Enum):
    json = "application/json"


@dataclass
class Encoding:
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#encodingObject
    """

    contentType: ContentType
    # headers: []


@dataclass
class MediaType:
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#mediaTypeObject
    """

    schema: Schema
    examples: t.Optional[t.Any] = None
    # encoding: dict[str, Encoding]


@dataclass
class Response:
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#responseObject
    """

    description: str
    # headers: {}
    # links: {}
    content: t.Optional[dict[ContentType, MediaType]] = None


class InParameterChoice(Enum):
    query = "query"
    header = "header"
    path = "path"
    cookie = "cookie"


@dataclass
class Parameter:
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#parameterObject
    """

    name: str
    in__: InParameterChoice
    required: bool = False
    description: t.Optional[str] = None
    allowEmptyValue: bool = False
    schema: t.Optional[Schema] = None


@dataclass
class RequestBody:
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#requestBodyObject
    """

    description: str
    content: dict[ContentType, MediaType]
    required: bool = False


@dataclass
class Operation:
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#operationObject
    """

    responses: dict[str, Response]
    operationId: str
    requestBody: t.Optional[RequestBody] = None
    tags: t.Optional[t.Sequence[str]] = None
    parameters: t.Optional[t.Sequence[Parameter]] = None
    summary: t.Optional[str] = None
    description: t.Optional[str] = None


@dataclass
class Path:
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#pathItemObject
    """

    get: t.Optional[Operation] = None
    post: t.Optional[Operation] = None
    put: t.Optional[Operation] = None
