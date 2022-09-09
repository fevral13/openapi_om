import typing as t
from pydantic import BaseModel

ListOfTuples = list[tuple[t.Any, t.Any]]


class BaseModelOptimizedRepr(BaseModel):
    def __repr_args__(self) -> ListOfTuples:
        result = super().__repr_args__()
        return [(k, v) for k, v in result if v is not None]
