from uuid import UUID

from pydantic import BaseModel


class GetTodoQuery(BaseModel):
    task_id: UUID
