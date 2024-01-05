import typing as t
from pydantic import Field, root_validator

from openapi_om.enums import (
    ContentType,
    SchemaType,
    PropertyFormat,
    InParameterChoice,
    SecuritySchemeChoice,
    InSecuritySchemeChoice,
)
from openapi_om.utils import BaseModelOptimizedRepr

__all__ = [
    "Components",
    "Contact",
    "Discriminator",
    "Encoding",
    "Example",
    "ExternalDocumentation",
    "Header",
    "Info",
    "License",
    "Link",
    "MediaType",
    "OauthFlow",
    "OauthFlows",
    "OpenAPI",
    "Operation",
    "Parameter",
    "Path",
    "RequestBody",
    "Response",
    "Schema",
    "SecurityScheme",
    "Server",
    "Tag",
    "XML",
]

DictAny = dict[t.Any, t.Any]
DictStrAny = dict[str, t.Any]
ListOfTuples = list[tuple[t.Any, t.Any]]


class Example(BaseModelOptimizedRepr):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#exampleObject
    """

    summary: t.Optional[str] = None
    """Short description for the example."""

    description: t.Optional[str] = None
    """Long description for the example. CommonMark syntax MAY be used for rich text representation."""

    externalValue: t.Optional[str] = None
    """A URL that points to the literal example. This provides the capability to reference examples that cannot 
    easily be included in JSON or YAML documents. The value field and externalValue field are mutually exclusive. """

    value: t.Optional[t.Any] = None
    """Embedded literal example. The value field and externalValue field are mutually exclusive. To represent 
    examples of media types that cannot naturally represented in JSON or YAML, use a string value to contain the 
    example, escaping where necessary. """


class ExternalDocumentation(BaseModelOptimizedRepr):
    """
    Allows referencing an external resource for extended documentation.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#externalDocumentationObject
    """

    url: str
    """REQUIRED. The URL for the target documentation. Value MUST be in the format of a URL."""

    description: t.Optional[str] = None
    """A short description of the target documentation. CommonMark syntax MAY be used for rich text representation."""


class Tag(BaseModelOptimizedRepr):
    """
    Adds metadata to a single tag that is used by the Operation Object. It is
    not mandatory to have a Tag Object per tag defined in the Operation Object instances.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#tagObject
    """

    name: str
    """REQUIRED. The name of the tag."""

    description: str = ""
    """A short description for the tag. CommonMark syntax MAY be used for rich text representation."""

    externalDocs: t.Optional[ExternalDocumentation] = None
    """Additional external documentation for this tag."""


class Contact(BaseModelOptimizedRepr):
    """
    Contact information for the exposed API.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#contactObject
    """

    name: t.Optional[str] = None
    """The identifying name of the contact person/organization."""

    email: t.Optional[str] = None
    """The URL pointing to the contact information. MUST be in the format of a URL."""

    url: t.Optional[str] = None
    """The email address of the contact person/organization. MUST be in the format of an email address."""


class License(BaseModelOptimizedRepr):
    """
    License information for the exposed API.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#licenseObject
    """

    name: str
    """REQUIRED. The license name used for the API."""

    url: t.Optional[str] = None
    """A URL to the license used for the API. MUST be in the format of a URL."""


class ServerVariable(BaseModelOptimizedRepr):
    """
    An object representing a Server Variable for server URL template substitution.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#serverVariableObject
    """

    default: str
    """REQUIRED. The default value to use for substitution, and to send, if an alternate value is not supplied. 
    Unlike the Schema Object's default, this value MUST be provided by the consumer. """

    enum: t.Optional[list[str]] = None
    """An enumeration of string values to be used if the substitution options are from a limited set."""

    description: t.Optional[str] = None
    """An optional description for the server variable. CommonMark syntax MAY be used for rich text representation."""


class Server(BaseModelOptimizedRepr):
    """
    An object representing a Server.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#serverObject
    """

    url: str
    """REQUIRED. A URL to the target host. This URL supports Server Variables and MAY be relative, to indicate that 
    the host location is relative to the location where the OpenAPI document is being served. Variable substitutions 
    will be made when a variable is named in {brackets}. """

    description: t.Optional[str] = None
    """An optional string describing the host designated by the URL. CommonMark syntax MAY be used for rich text 
    representation. """

    variables: t.Optional[dict[str, ServerVariable]] = None
    """A map between a variable name and its value. The value is used for substitution in the server's URL template."""


class Info(BaseModelOptimizedRepr):
    """
    The object provides metadata about the API. The metadata MAY be used by the clients if needed, and MAY be
    presented in editing or documentation generation tools for convenience.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#infoObject
    """

    title: str
    """REQUIRED. The title of the application."""

    version: str
    """REQUIRED. The version of the OpenAPI document (which is distinct from the OpenAPI Specification version or the 
    API implementation version). """

    contact: t.Optional[Contact] = None
    """The contact information for the exposed API."""

    description: t.Optional[str] = None
    """A short description of the application. CommonMark syntax MAY be used for rich text representation."""

    termsOfService: t.Optional[str] = None
    """A URL to the Terms of Service for the API. MUST be in the format of a URL."""

    license: t.Optional["License"] = None
    """The license information for the exposed API."""


class Discriminator(BaseModelOptimizedRepr):
    """
    When request bodies or response payloads may be one of a number of different schemas, a discriminator
    object can be used to aid in serialization, deserialization, and validation. The discriminator is a
    specific object in a schema which is used to inform the consumer of the specification of an alternative
    schema based on the value associated with it.

    When using the discriminator, inline schemas will not be considered.

    The discriminator attribute is legal only when using one of the composite keywords oneOf, anyOf, allOf.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#discriminatorObject
    """

    propertyName: str
    """REQUIRED. The name of the property in the payload that will hold the discriminator value."""

    mapping: t.Optional[dict[str, str]] = None
    """An object to hold mappings between payload values and schema names or references."""


class XML(BaseModelOptimizedRepr):
    """
    A metadata object that allows for more fine-tuned XML model definitions.

    When using arrays, XML element names are not inferred (for singular/plural forms) and the name property
    SHOULD be used to add that information. See examples for expected behavior.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#xmlObject
    """

    name: t.Optional[str] = None
    """Replaces the name of the element/attribute used for the described schema property. When defined within items, 
    it will affect the name of the individual XML elements within the list. When defined alongside type being array (
    outside the items), it will affect the wrapping element and only if wrapped is true. If wrapped is false, 
    it will be ignored. """

    namespace: t.Optional[str] = None
    """The URI of the namespace definition. Value MUST be in the form of an absolute URI."""

    prefix: t.Optional[str] = None
    """The prefix to be used for the name."""

    attribute: t.Optional[bool] = None
    """Declares whether the property definition translates to an attribute instead of an element. Default value is 
    false. """

    wrapped: t.Optional[bool] = None
    """MAY be used only for an array definition. Signifies whether the array is wrapped (for example, 
    <books><book/><book/></books>) or unwrapped (<book/><book/>). Default value is false. The definition takes effect 
    only when defined alongside type being array (outside the items). """


class Schema(BaseModelOptimizedRepr):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#schemaObject
    """

    # todo validate object
    type: t.Optional[SchemaType] = None
    properties: t.Optional[dict[str, "Schema"]] = None
    items: t.Optional["Schema"] = None

    required: t.Optional[list[str]] = None
    readOnly: t.Optional[bool] = None
    """Relevant only for Schema "properties" definitions. Declares the property as "read only". This means that it 
    MAY be sent as part of a response but SHOULD NOT be sent as part of the request. If the property is marked as 
    readOnly being true and is in the required list, the required will take effect on the response only. A property 
    MUST NOT be marked as both readOnly and writeOnly being true. Default value is false. """

    writeOnly: t.Optional[bool] = None
    """Relevant only for Schema "properties" definitions. Declares the property as "write only". Therefore, 
    it MAY be sent as part of a request but SHOULD NOT be sent as part of the response. If the property is marked as 
    writeOnly being true and is in the required list, the required will take effect on the request only. A property 
    MUST NOT be marked as both readOnly and writeOnly being true. Default value is false. """

    nullable: t.Optional[bool] = None
    """Allows sending a null value for the defined schema. Default value is false."""

    deprecated: t.Optional[bool] = None
    """Specifies that a schema is deprecated and SHOULD be transitioned out of usage. Default value is false."""

    externalDocs: t.Optional[ExternalDocumentation] = None
    """Additional external documentation for this schema."""

    example: t.Optional[t.Any] = None
    """A free-form property to include an example of an instance for this schema. To represent examples that cannot 
    be naturally represented in JSON or YAML, a string value can be used to contain the example with escaping where 
    necessary. """

    discriminator: t.Optional[Discriminator] = None
    """Adds support for polymorphism. The discriminator is an object name that is used to differentiate between other 
    schemas which may satisfy the payload description. See Composition and Inheritance for more details. """

    xml: t.Optional[XML] = None
    """This MAY be used only on properties schemas. It has no effect on root schemas. Adds additional metadata to 
    describe the XML representation of this property. """

    minimum: t.Optional[int] = None
    exclusiveMinimum: t.Optional[int] = None
    maximum: t.Optional[int] = None
    exclusiveMaximum: t.Optional[int] = None
    maxLength: t.Optional[int] = None
    minLength: t.Optional[int] = None
    pattern: t.Optional[str] = None
    maxItems: t.Optional[int] = None
    minItems: t.Optional[int] = None
    maxProperties: t.Optional[int] = None
    minProperties: t.Optional[int] = None
    uniqueItems: t.Optional[bool] = None
    enum: t.Optional[t.Sequence[str]] = None

    format: t.Optional[PropertyFormat] = None
    title: t.Optional[str] = None
    description: t.Optional[str] = None
    additionalProperties: t.Optional[t.Union[bool, "Schema"]] = None
    default: t.Optional[t.Any] = None
    """The default value represents what would be assumed by the consumer of the input as the value of the schema if 
    one is not provided. Unlike JSON Schema, the value MUST conform to the defined type for the Schema Object defined 
    at the same level. For example, if type is string, then default can be "foo" but cannot be 1. """

    allOf: t.Optional[t.Sequence["Schema"]] = None
    anyOf: t.Optional[t.Sequence["Schema"]] = None
    oneOf: t.Optional[t.Sequence["Schema"]] = None
    not_: t.Optional["Schema"] = Field(default=None, alias="not")

    multipleOf: t.Optional[int] = None
    """The value of "multipleOf" MUST be a number, strictly greater than 0.

    A numeric instance is only valid if division by this keyword's value
    results in an integer."""

    @root_validator(pre=True)
    def map_not_name(cls, values: DictAny) -> DictAny:
        if "not" in values:
            values["not_"] = values.pop("not")
        return values

    # def __post_init__(self):
    #     if self.type == SchemaType.object:
    #         self._validate_object()
    #
    # def _validate_object(self):
    #     if self.properties is None:
    #         raise ValidationError(
    #             f"""Schema {self} is of type "object" should define `properties`""",
    #             schema_object=self,
    #         )
    #     if self.required is None:
    #         raise ValidationError(
    #             """`required` property must be set for type "object" """,
    #             schema_object=self,
    #         )
    #     set_of_properties = {prop_name for prop_name in self.properties.keys()}
    #     set_of_required = set(self.required)
    #
    #     unknown = set_of_required - set_of_properties
    #     if unknown:
    #         raise ValidationError(
    #             f"These properties {unknown} are required, but are missing in property list.",
    #             schema_object=self,
    #         )


class Parameter(BaseModelOptimizedRepr):
    """
    Describes a single operation parameter.

    A unique parameter is defined by a combination of a name and location.

    Parameter Locations

    There are four possible parameter locations specified by the in field:

    - path - Used together with Path Templating, where the parameter value is actually part of the operation's URL.
    This does not include the host or base path of the API. For example, in /items/{itemId}, the path parameter is
    itemId.

    - query - Parameters that are appended to the URL. For example, in /items?id=###, the query parameter is
    id.

    - header - Custom headers that are expected as part of the request. Note that RFC7230 states header names are
    case-insensitive.

    - cookie - Used to pass a specific cookie value to the API.


    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#parameterObject
    """

    name: str
    """
    REQUIRED. The name of the parameter. Parameter names are case sensitive.

    If in is "path", the name field MUST correspond to the associated path segment from the path field in 
    the Paths Object. See Path Templating for further information.
    
    If in is "header" and the name field is "Accept", "Content-Type" or "Authorization", the parameter 
    definition SHALL be ignored.
    
    For all other cases, the name corresponds to the parameter name used by the in property.
    """

    in_: InParameterChoice
    """REQUIRED. The location of the parameter. Possible values are "query", "header", "path" or "cookie"."""

    required: bool = False
    """Determines whether this parameter is mandatory. If the parameter location is "path", this property is REQUIRED 
    and its value MUST be true. Otherwise, the property MAY be included and its default value is false. """

    description: t.Optional[str] = None
    """A brief description of the parameter. This could contain examples of use. CommonMark syntax MAY be used for 
    rich text representation. """

    allowEmptyValue: bool = False
    """Sets the ability to pass empty-valued parameters. This is valid only for query parameters and allows sending a 
    parameter with an empty value. Default value is false. If style is used, and if behavior is n/a (cannot be 
    serialized), the value of allowEmptyValue SHALL be ignored. """

    deprecated: t.Optional[bool] = None
    """Specifies that a parameter is deprecated and SHOULD be transitioned out of usage."""

    schema_: t.Optional[Schema] = Field(default=None, alias="schema")
    """The schema defining the type used for the parameter."""

    style: t.Optional[str] = None
    """Describes how the parameter value will be serialized depending on the type of the parameter value. Default 
    values (based on value of in): for query - form; for path - simple; for header - simple; for cookie - form. """

    explode: t.Optional[bool] = None
    """When this is true, parameter values of type array or object generate separate parameters for each value of the 
    array or key-value pair of the map. For other types of parameters this property has no effect. When style is 
    form, the default value is true. For all other styles, the default value is false. """

    allowReserved: t.Optional[bool] = None
    """Determines whether the parameter value SHOULD allow reserved characters, as defined by RFC3986 :/?#[]@!$&'(
    )*+,;= to be included without percent-encoding. This property only applies to parameters with an in value of 
    query. The default value is false. """

    example: t.Optional[t.Any] = None
    """Example of the media type. The example SHOULD match the specified schema and encoding properties if present. 
    The example field is mutually exclusive of the examples field. Furthermore, if referencing a schema which 
    contains an example, the example value SHALL override the example provided by the schema. To represent examples 
    of media types that cannot naturally be represented in JSON or YAML, a string value can contain the example with 
    escaping where necessary. """

    examples: t.Optional[dict[str, Example]] = None
    """Examples of the media type. Each example SHOULD contain a value in the correct format as specified in the 
    parameter encoding. The examples field is mutually exclusive of the example field. Furthermore, if referencing a 
    schema which contains an example, the examples value SHALL override the example provided by the schema. """

    @root_validator(pre=True)
    def map_in_name(cls, values: DictAny) -> DictAny:
        if "in" in values:
            values["in_"] = values.pop("in")
        return values

    def dict(self, *args: t.Any, **kwargs: t.Any) -> DictStrAny:
        result = super().dict(*args, **kwargs)
        result["in"] = result.pop("in_")
        return result

    def __repr_args__(self) -> ListOfTuples:
        result = super().__repr_args__()
        return [("schema" if k == "schema_" else k, v) for k, v in result]


class Header(BaseModelOptimizedRepr):
    """
    The Header Object follows the structure of the Parameter Object with the following changes:

    - name MUST NOT be specified, it is given in the corresponding headers map.
    - in MUST NOT be specified, it is implicitly in header.
    - All traits that are affected by the location MUST be applicable to a location of header (for example, style).


    Example:

      {
          "description": "The number of allowed requests in the current period",
          "schema": {
              "type": "integer"
          }
      }

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#header-object
    """

    required: bool = False
    description: t.Optional[str] = None
    allowEmptyValue: bool = False
    schema_: t.Optional[Schema] = Field(default=None, alias="schema")
    example: t.Optional[t.Any] = None
    examples: t.Optional[dict[str, Example]] = None

    def __repr_args__(self) -> ListOfTuples:
        result = super().__repr_args__()
        return [("schema" if k == "schema_" else k, v) for k, v in result]


class Encoding(BaseModelOptimizedRepr):
    """
    A single encoding definition applied to a single schema property.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#encodingObject
    """

    contentType: t.Optional[t.Union[ContentType, str]] = None
    """The Content-Type for encoding a specific property. Default value depends on the property type: for string with 
    format being binary – application/octet-stream; for other primitive types – text/plain; for object - 
    application/json; for array – the default is defined based on the inner type. The value can be a specific media 
    type (e.g. application/json), a wildcard media type (e.g. image/*), or a comma-separated list of the two types. """

    headers: t.Optional[dict[str, Header]] = None
    """A map allowing additional information to be provided as headers, for example Content-Disposition. Content-Type 
    is described separately and SHALL be ignored in this section. This property SHALL be ignored if the request body 
    media type is not a multipart. """

    style: t.Optional[str] = None
    """Describes how a specific property value will be serialized depending on its type. See Parameter Object for 
    details on the style property. The behavior follows the same values as query parameters, including default 
    values. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded. """

    explode: t.Optional[bool] = None
    """When this is true, property values of type array or object generate separate parameters for each value of the 
    array, or key-value-pair of the map. For other types of properties this property has no effect. When style is 
    form, the default value is true. For all other styles, the default value is false. This property SHALL be ignored 
    if the request body media type is not application/x-www-form-urlencoded. """

    allowReserved: t.Optional[bool] = None
    """Determines whether the parameter value SHOULD allow reserved characters, as defined by RFC3986 :/?#[]@!$&'(
    )*+,;= to be included without percent-encoding. The default value is false. This property SHALL be ignored if the 
    request body media type is not application/x-www-form-urlencoded. """


class MediaType(BaseModelOptimizedRepr):
    """
    Each Media Type Object provides schema and examples for the media type identified by its key.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#mediaTypeObject
    """

    schema_: Schema = Field(alias="schema")
    """The schema defining the type used for the request body."""

    example: t.Optional[t.Any] = None
    """Example of the media type. The example object SHOULD be in the correct format as specified by the media type. 
    The example field is mutually exclusive of the examples field. Furthermore, if referencing a schema which 
    contains an example, the example value SHALL override the example provided by the schema. """

    examples: t.Optional[dict[str, Example]] = None
    """Examples of the media type. Each example object SHOULD match the media type and specified schema if present. 
    The examples field is mutually exclusive of the example field. Furthermore, if referencing a schema which 
    contains an example, the examples value SHALL override the example provided by the schema. """

    encoding: t.Optional[dict[str, Encoding]] = None
    """A map between a property name and its encoding information. The key, being the property name, MUST exist in 
    the schema as a property. The encoding object SHALL only apply to requestBody objects when the media type is 
    multipart or application/x-www-form-urlencoded. """

    def __repr_args__(self) -> ListOfTuples:
        result = super().__repr_args__()
        return [("schema" if k == "schema_" else k, v) for k, v in result]


class Link(BaseModelOptimizedRepr):
    """
    The Link object represents a possible design-time link for a response.
    The presence of a link does not guarantee the caller's ability to successfully
    invoke it, rather it provides a known relationship and traversal mechanism between
    responses and other operations.

    Unlike dynamic links (i.e. links provided in the response payload), the OAS linking
    mechanism does not require link information in the runtime response.

    For computing links, and providing instructions to execute them, a runtime expression
    is used for accessing values in an operation and using them as parameters while invoking
    the linked operation.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#linkObject
    """

    operationRef: t.Optional[str] = None
    """A relative or absolute reference to an OAS operation. This field is mutually exclusive of the operationId 
    field, and MUST point to an Operation Object. Relative operationRef values MAY be used to locate an existing 
    Operation Object in the OpenAPI definition. """

    operationId: t.Optional[str] = None
    """The name of an existing, resolvable OAS operation, as defined with a unique operationId. This field is 
    mutually exclusive of the operationRef field. """

    parameters: t.Optional[dict[str, t.Any]] = None
    """A map representing parameters to pass to an operation as specified with operationId or identified via 
    operationRef. The key is the parameter name to be used, whereas the value can be a constant or an expression to 
    be evaluated and passed to the linked operation. The parameter name can be qualified using the parameter location 
    [{in}.]{name} for operations that use the same parameter name in different locations (e.g. path.id). """

    requestBody: t.Optional[t.Any] = None
    """A literal value or {expression} to use as a request body when calling the target operation."""

    description: t.Optional[str] = None
    """A description of the link. CommonMark syntax MAY be used for rich text representation."""

    server: t.Optional[Server] = None
    """A server object to be used by the target operation."""


class Response(BaseModelOptimizedRepr):
    """
    Describes a single response from an API Operation, including design-time,
    static links to operations based on the response.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#responseObject
    """

    description: str
    """REQUIRED. A short description of the response. CommonMark syntax MAY be used for rich text representation."""

    headers: t.Optional[dict[str, Header]] = None
    """Maps a header name to its definition. RFC7230 states header names are case insensitive. If a response header 
    is defined with the name "Content-Type", it SHALL be ignored. """

    links: t.Optional[dict[str, Link]] = None
    """A map containing descriptions of potential response payloads. The key is a media type or media type range and 
    the value describes it. For responses that match multiple keys, only the most specific key is applicable. e.g. 
    text/plain overrides text/* """

    content: t.Optional[dict[t.Union[ContentType, str], MediaType]] = None
    """A map of operations links that can be followed from the response. The key of the map is a short name for the 
    link, following the naming constraints of the names for Component Objects. """

    def dict(self, *args: t.Any, **kwargs: t.Any) -> DictStrAny:
        result = super().dict(*args, **kwargs)

        if result.get("content") is not None:
            result["content"] = {
                str(key.value): value for key, value in result["content"].items()
            }
        return result


class RequestBody(BaseModelOptimizedRepr):
    """
    Describes a single request body.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#requestBodyObject
    """

    content: dict[t.Union[ContentType, str], MediaType]
    """REQUIRED. The content of the request body. The key is a media type or media type range and the value describes 
    it. For requests that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides 
    text/* """

    description: t.Optional[str] = None
    """A brief description of the request body. This could contain examples of use. CommonMark syntax MAY be used for 
    rich text representation. """

    required: bool = False
    """Determines if the request body is required in the request. Defaults to false."""

    def dict(self, *args: t.Any, **kwargs: t.Any) -> DictStrAny:
        result = super().dict(*args, **kwargs)

        result["content"] = {
            str(key.value): value for key, value in result["content"].items()
        }
        return result


class Callback(BaseModelOptimizedRepr):
    """
    A map of possible out-of band callbacks related to the parent operation.
    Each value in the map is a Path Item Object that describes a set of requests
    that may be initiated by the API provider and the expected responses. The key value
    used to identify the callback object is an expression, evaluated at runtime, that
    identifies a URL to use for the callback operation.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#callbackObject
    """


class SecurityRequirement(BaseModelOptimizedRepr):
    """
    Lists the required security schemes to execute this operation. The name used for
    each property MUST correspond to a security scheme declared in the Security Schemes
    under the Components Object.

    Security Requirement Objects that contain multiple schemes require that all schemes
    MUST be satisfied for a request to be authorized. This enables support for scenarios
    where multiple query parameters or HTTP headers are required to convey security information.

    When a list of Security Requirement Objects is defined on the Open API object or
    Operation Object, only one of Security Requirement Objects in the list needs to be
    satisfied to authorize the request.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#securityRequirementObject
    """


class Operation(BaseModelOptimizedRepr):
    """
    Describes a single API operation on a path.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#operationObject
    """

    responses: dict[int, Response]
    """REQUIRED. The list of possible responses as they are returned from executing this operation."""

    operationId: t.Optional[str] = None
    """Unique string used to identify the operation. The id MUST be unique among all operations described in the API. 
    Tools and libraries MAY use the operationId to uniquely identify an operation, therefore, it is RECOMMENDED to 
    follow common programming naming conventions. """

    requestBody: t.Optional[RequestBody] = None
    """The request body applicable for this operation. The requestBody is only supported in HTTP methods where the 
    HTTP 1.1 specification RFC7231 has explicitly defined semantics for request bodies. In other cases where the HTTP 
    spec is vague, requestBody SHALL be ignored by consumers. """

    tags: t.Optional[t.Sequence[str]] = None
    """A list of tags for API documentation control. Tags can be used for logical grouping of operations by resources 
    or any other qualifier. """

    parameters: t.Optional[t.Sequence[Parameter]] = None
    """A list of parameters that are applicable for this operation. If a parameter is already defined at the Path 
    Item, the new definition will override it but can never remove it. The list MUST NOT include duplicated 
    parameters. A unique parameter is defined by a combination of a name and location. The list can use the Reference 
    Object to link to parameters that are defined at the OpenAPI Object's components/parameters. """

    summary: t.Optional[str] = None
    """A short summary of what the operation does."""

    description: t.Optional[str] = None
    """A verbose explanation of the operation behavior. CommonMark syntax MAY be used for rich text representation."""

    externalDocs: t.Optional[ExternalDocumentation] = None
    """Additional external documentation for this operation."""

    deprecated: bool = False
    """Declares this operation to be deprecated. Consumers SHOULD refrain from usage of the declared operation. 
    Default value is false. """

    servers: t.Optional[t.Sequence[Server]] = None
    """An alternative server array to service this operation. If an alternative server object is specified at the 
    Path Item Object or Root level, it will be overridden by this value. """

    callbacks: t.Optional[dict[str, Callback]] = None
    """A map of possible out-of band callbacks related to the parent operation. The key is a unique identifier for 
    the Callback Object. Each value in the map is a Callback Object that describes a request that may be initiated by 
    the API provider and the expected responses. The key value used to identify the callback object is an expression, 
    evaluated at runtime, that identifies a URL to use for the callback operation. """

    security: t.Optional[list[SecurityRequirement]] = None
    """A declaration of which security mechanisms can be used for this operation. The list of values includes 
    alternative security requirement objects that can be used. Only one of the security requirement objects need to 
    be satisfied to authorize a request. This definition overrides any declared top-level security. To remove a 
    top-level security declaration, an empty array can be used. """


class Path(BaseModelOptimizedRepr):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#pathItemObject
    """

    summary: t.Optional[str] = None
    """An optional, string summary, intended to apply to all operations in this path."""

    description: t.Optional[str] = None
    """An optional, string description, intended to apply to all operations in this path. CommonMark syntax MAY be 
    used for rich text representation. """

    get: t.Optional[Operation] = None
    put: t.Optional[Operation] = None
    post: t.Optional[Operation] = None
    delete: t.Optional[Operation] = None
    options: t.Optional[Operation] = None
    head: t.Optional[Operation] = None
    patch: t.Optional[Operation] = None
    trace: t.Optional[Operation] = None
    servers: t.Optional[t.Sequence[Server]] = None
    """An alternative server array to service all operations in this path."""

    parameters: t.Optional[t.Sequence[Parameter]] = None
    """A list of parameters that are applicable for all the operations described under this path. These parameters 
    can be overridden at the operation level, but cannot be removed there. The list MUST NOT include duplicated 
    parameters. A unique parameter is defined by a combination of a name and location. The list can use the Reference 
    Object to link to parameters that are defined at the OpenAPI Object's components/parameters. """


class OauthFlow(BaseModelOptimizedRepr):
    """
    Configuration details for a supported OAuth Flow

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#oauth-flow-object
    """

    # todo: validate object
    authorizationUrl: t.Optional[str] = None
    """Applies to oauth2 ("implicit", "authorizationCode"). REQUIRED. The authorization URL to be used for this flow. 
    This MUST be in the form of a URL. """

    tokenUrl: t.Optional[str] = None
    """Applies to oauth2 ("password", "clientCredentials", "authorizationCode"). REQUIRED. The token URL to be used 
    for this flow. This MUST be in the form of a URL. """

    refreshUrl: t.Optional[str] = None
    """The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL."""

    scopes: t.Optional[dict[str, str]] = None
    """REQUIRED. The available scopes for the OAuth2 security scheme. A map between the scope name and a short 
    description for it. """


class OauthFlows(BaseModelOptimizedRepr):
    """
    Allows configuration of the supported OAuth Flows.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#oauth-flows-object
    """

    implicit: t.Optional[OauthFlow] = None
    """Configuration for the OAuth Implicit flow"""

    password: t.Optional[OauthFlow] = None
    """Configuration for the OAuth Resource Owner Password flow"""

    clientCredentials: t.Optional[OauthFlow] = None
    """Configuration for the OAuth Client Credentials flow. Previously called application in OpenAPI 2.0."""

    authorizationCode: t.Optional[OauthFlow] = None
    """Configuration for the OAuth Authorization Code flow. Previously called accessCode in OpenAPI 2.0."""


class SecurityScheme(BaseModelOptimizedRepr):
    """
    Defines a security scheme that can be used by the operations. Supported schemes are HTTP authentication,
    an API key (either as a header or as a query parameter), OAuth2's common flows (implicit, password,
    application and access code) as defined in RFC6749, and OpenID Connect Discovery.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#securitySchemeObject
    """

    # todo: validate object

    type: SecuritySchemeChoice
    """REQUIRED. The type of the security scheme. Valid values are "apiKey", "http", "oauth2", "openIdConnect"."""

    name: t.Optional[str] = None
    """Applies to apiKey. REQUIRED. The name of the header, query or cookie parameter to be used. """

    in_: t.Optional[InSecuritySchemeChoice] = Field(default=None, alias="in")
    """Applies to apiKey. REQUIRED. The location of the API key. Valid values are "query", "header" or "cookie". """

    scheme: t.Optional[str] = None
    """Applies to http. REQUIRED. The name of the HTTP Authorization scheme to be used in the Authorization header as 
    defined in RFC7235. """

    bearerFormat: t.Optional[str] = None
    """Applies to http. A hint to the client to identify how the bearer token is formatted. Bearer tokens are usually 
    generated by an authorization server, so this information is primarily for documentation purposes. """

    flows: t.Optional[OauthFlows] = None
    """Applies to oauth2. REQUIRED. An object containing configuration information for the flow types supported."""

    openIdConnectUrl: t.Optional[str] = None
    """Applies to openIdConnect. REQUIRED. OpenId Connect URL to discover OAuth2 configuration values. This MUST be 
    in the form of a URL. """

    description: t.Optional[str] = None
    """A short description for security scheme. CommonMark syntax MAY be used for rich text representation."""

    @root_validator(pre=True)
    def map_in_name(cls, values: DictAny) -> DictAny:
        if "in" in values:
            values["in_"] = values.pop("in")
        return values


class Components(BaseModelOptimizedRepr):
    """
    Holds a set of reusable objects for different aspects of the OAS. All objects defined within the
    components object will have no effect on the API unless they are explicitly referenced from properties
    outside the components object.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#componentsObject
    """

    schemas: t.Optional[dict[str, Schema]] = None
    responses: t.Optional[dict[str, Response]] = None
    parameters: t.Optional[dict[str, Parameter]] = None
    examples: t.Optional[dict[str, Example]] = None
    requestBodies: t.Optional[dict[str, RequestBody]] = None
    headers: t.Optional[dict[str, Header]] = None
    securitySchemes: t.Optional[dict[str, SecurityScheme]] = None
    links: t.Optional[dict[str, Link]] = None
    callbacks: t.Optional[dict[str, Callback]] = None


class OpenAPI(BaseModelOptimizedRepr):
    """
    This is the root document object of the OpenAPI document.

    Main class and entrypoint for OpenAPI schema definition.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#oasObject
    """

    info: "Info"
    """REQUIRED. Provides metadata about the API. The metadata MAY be used by tooling as required."""

    paths: dict[str, Path]
    """REQUIRED. The available paths and operations for the API."""

    openapi: str = "3.0.1"
    """REQUIRED. This string MUST be the semantic version number of the OpenAPI Specification version that the 
    OpenAPI document uses. The openapi field SHOULD be used by tooling specifications and clients to interpret the 
    OpenAPI document. This is not related to the API info.version string. """

    tags: t.Optional[t.Sequence[Tag]] = None
    """A list of tags used by the specification with additional metadata. The order of the tags can be used to 
    reflect on their order by the parsing tools. Not all tags that are used by the Operation Object must be declared. 
    The tags that are not declared MAY be organized randomly or based on the tools' logic. Each tag name in the list 
    MUST be unique. """

    externalDocs: t.Optional[ExternalDocumentation] = None
    """Additional external documentation."""

    # If the servers property is not provided, or is an empty array,
    # the default value would be a Server Object with an url value of /.
    servers: list["Server"] = Field(
        default_factory=lambda: [Server(url="/", description="Default server")]
    )

    security: t.Optional[SecurityRequirement] = None
    """A declaration of which security mechanisms can be used across the API. The list of values includes alternative 
    security requirement objects that can be used. Only one of the security requirement objects need to be satisfied 
    to authorize a request. Individual operations can override this definition. """

    components: t.Optional[Components] = None
    """An element to hold various schemas for the specification."""
