from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from src.domain.todos import ToDo


class UpdateTodoResponse(BaseModel):
    status: str = 'OK'


class GetTodoDetailsResponse(BaseModel):
    id: UUID
    title: str
    date_created: datetime
    date_updated: Optional[datetime]

    @staticmethod
    def from_data(todo: ToDo) -> GetTodoDetailsResponse:
        return GetTodoDetailsResponse(
            id=todo.id,
            title=todo.title,
            date_created=todo.date_created,
            date_updated=todo.date_updated,
        )


class GetTodoListResponse(BaseModel):
    tasks: list[GetTodoDetailsResponse]

    @staticmethod
    def from_data(tasks: list[ToDo]) -> GetTodoListResponse:
        return GetTodoListResponse(tasks=[GetTodoDetailsResponse.from_data(task) for task in tasks])
