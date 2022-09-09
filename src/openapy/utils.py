from pydantic import BaseModel


class BaseModelOptimizedRepr(BaseModel):
    def __repr_args__(self):
        result = super().__repr_args__()
        return [(k, v) for k, v in result if v is not None]
