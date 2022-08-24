from dataclasses import dataclass, field


__all__ = ["Server"]


@dataclass
class Server:
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#serverObject
    """

    url: str
    description: str = ""
