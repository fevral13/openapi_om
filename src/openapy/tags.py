from dataclasses import dataclass


__all__ = ["Tag"]


@dataclass
class Tag:
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#tagObject
    """

    name: str
    description: str = ""
