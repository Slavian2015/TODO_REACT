from uuid import UUID

from pydantic import BaseModel


class CreateTodoCommand(BaseModel):
    title: str


class UpdateTodoCommand(BaseModel):
    task_id: UUID
    title: str


class DeleteTodoCommand(BaseModel):
    task_id: UUID
