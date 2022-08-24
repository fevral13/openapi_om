import json
import typing as t
from dataclasses import dataclass, field, asdict

import yaml

from openapy.paths import Path
from openapy.server import Server
from openapy.tags import Tag
from openapy.utils import remove_nulls, Encoder

__all__ = ["OpenAPI", "Contact", "Info"]


@dataclass
class Contact:
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#contactObject
    """

    name: str
    email: str


@dataclass
class Info:
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#infoObject
    """

    title: str
    version: str
    description: str
    contact: Contact


@dataclass
class OpenAPI:
    """
    Main class and entrypoint for OpenAPI schema definition.

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#oasObject
    """

    info: Info
    openapi: str = "3.0.1"
    paths: dict[str, Path] = field(default_factory=dict)
    tags: t.Sequence[Tag] = ()

    # If the servers property is not provided, or is an empty array,
    # the default value would be a Server Object with an url value of /.
    servers: t.Sequence[Server] = field(
        default_factory=lambda: [Server(url="/", description="Default server")]
    )

    def as_dict(self) -> dict[str, t.Any]:
        schema_dict = asdict(self)
        remove_nulls(schema_dict)
        return schema_dict

    def as_json(self, **kwargs) -> str:
        return json.dumps(self.as_dict(), cls=Encoder, **kwargs)

    def as_yaml(self) -> str:
        schema_dict = json.loads(self.as_json())
        return yaml.dump(schema_dict, explicit_start=True)
