from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from src.value_object.value_object import TodoTitle


class CreateTodoRequest(BaseModel):
    title: str = Field(..., min_length=3, max_length=30)

    @validator('title')
    def title_format(cls, title: str) -> str:
        return str(TodoTitle(title))


class UpdateTodoRequest(BaseModel):
    title: str = Field(..., min_length=3, max_length=30)

    @validator('title')
    def title_format(cls, title: str) -> str:
        return str(TodoTitle(title))
