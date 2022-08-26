import typing as t
from dataclasses import dataclass, field

from openapy.utils import BaseNode, ValidationError
from openapy.enums import ContentType, SchemaType, PropertyFormat, InParameterChoice

__all__ = [
    "Contact",
    "Encoding",
    "ExternalDocumentation",
    "Info",
    "License",
    "MediaType",
    "OpenAPI",
    "Operation",
    "Parameter",
    "Path",
    "RequestBody",
    "Response",
    "Schema",
    "Server",
    "Tag",
]


@dataclass
class OpenAPI(BaseNode):
    """
    Main class and entrypoint for OpenAPI schema definition.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#oasObject
    """

    info: "Info"
    paths: dict[str, "Path"]
    openapi: str = "3.0.1"
    tags: t.Sequence["Tag"] = ()
    externalDocs: t.Optional["ExternalDocumentation"] = None

    # If the servers property is not provided, or is an empty array,
    # the default value would be a Server Object with an url value of /.
    servers: t.Sequence["Server"] = field(
        default_factory=lambda: [Server(url="/", description="Default server")]
    )


@dataclass
class Info(BaseNode):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#infoObject
    """

    title: str
    version: str
    contact: t.Optional["Contact"] = None
    description: t.Optional[str] = None
    termsOfService: t.Optional[str] = None
    license: t.Optional["License"] = None


@dataclass
class Encoding(BaseNode):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#encodingObject
    """

    contentType: "ContentType"
    # headers: []


@dataclass
class MediaType(BaseNode):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#mediaTypeObject
    """

    schema: "Schema"
    examples: t.Optional[t.Any] = None
    # encoding: dict[str, Encoding]


@dataclass
class Response(BaseNode):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#responseObject
    """

    description: str
    # headers: {}
    # links: {}
    content: t.Optional[dict[ContentType, MediaType]] = None


@dataclass
class Parameter(BaseNode):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#parameterObject
    """

    name: str
    in__: InParameterChoice
    required: bool = False
    description: t.Optional[str] = None
    allowEmptyValue: bool = False
    schema: t.Optional["Schema"] = None


@dataclass
class RequestBody(BaseNode):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#requestBodyObject
    """

    description: str
    content: dict[ContentType, MediaType]
    required: bool = False


@dataclass
class Operation(BaseNode):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#operationObject
    """

    responses: dict[str, Response]
    operationId: t.Optional[str] = None
    requestBody: t.Optional[RequestBody] = None
    tags: t.Optional[t.Sequence[str]] = None
    parameters: t.Optional[t.Sequence[Parameter]] = None
    summary: t.Optional[str] = None
    description: t.Optional[str] = None
    externalDocs: t.Optional["ExternalDocumentation"] = None
    deprecated: bool = False
    servers: t.Optional[t.Sequence["Server"]] = None


@dataclass
class Path(BaseNode):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#pathItemObject
    """

    summary: t.Optional[str] = None
    description: t.Optional[str] = None
    get: t.Optional[Operation] = None
    put: t.Optional[Operation] = None
    post: t.Optional[Operation] = None
    delete: t.Optional[Operation] = None
    options: t.Optional[Operation] = None
    head: t.Optional[Operation] = None
    patch: t.Optional[Operation] = None
    trace: t.Optional[Operation] = None
    servers: t.Optional[t.Sequence["Server"]] = None
    parameters: t.Optional[t.Sequence[Parameter]] = None


@dataclass
class Tag(BaseNode):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#tagObject
    """

    name: str
    description: str = ""


@dataclass
class Server(BaseNode):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#serverObject
    """

    url: str
    description: str = ""


@dataclass
class Contact(BaseNode):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#contactObject
    """

    name: t.Optional[str] = None
    email: t.Optional[str] = None
    url: t.Optional[str] = None


@dataclass
class License(BaseNode):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#licenseObject
    """

    name: str
    url: t.Optional[str] = None


@dataclass
class ExternalDocumentation(BaseNode):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#externalDocumentationObject
    """

    url: str
    name: t.Optional[str] = None


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
    nullable: t.Optional[bool] = None
    minimum: t.Optional[int] = None
    format: t.Optional[PropertyFormat] = None
    enum: t.Optional[t.Sequence[str]] = None
    description: t.Optional[str] = None

    def __post_init__(self):
        if self.type == SchemaType.object:
            self._validate_object()

    def _validate_object(self):
        if self.properties is None:
            raise ValidationError(
                f"""Schema {self} is of type "object" should define `properties`""",
                schema_object=self,
            )
        if self.required is None:
            raise ValidationError(
                """`required` property must be set for type "object" """,
                schema_object=self,
            )
        set_of_properties = {prop_name for prop_name in self.properties.keys()}
        set_of_required = set(self.required)

        unknown = set_of_required - set_of_properties
        if unknown:
            raise ValidationError(
                f"These properties {unknown} are required, but are missing in property list.",
                schema_object=self,
            )
