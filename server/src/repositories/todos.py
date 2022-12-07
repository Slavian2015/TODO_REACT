from __future__ import annotations

from uuid import UUID

from src.domain.todos import ToDo
from src.mapping.todos import TodosTable
from src.repositories.abstract import AbstractAlchemyRepository
from src.repositories.errors import TaskNotExistsError
from src.repositories.errors import TaskExistsError
from src.repositories.interface import TodosRepositoryInterface


class TodosRepository(AbstractAlchemyRepository, TodosRepositoryInterface):

    def get_task_by_title(self, title: str) -> ToDo:
        task: ToDo | None = self.session.query(ToDo).where(TodosTable.c.title == title).one_or_none()
        if not task:
            raise TaskNotExistsError
        return task

    def create_task(self, task: ToDo) -> UUID:
        try:
            self.get_task_by_title(task.title)
            raise TaskExistsError('Task already exists')
        except TaskNotExistsError:
            ...
        self.session.add(task)
        return task.id

    def get_task_by_id(self, task_id: UUID) -> ToDo:
        task: ToDo | None = self.session.get(ToDo, task_id)
        if not task:
            raise TaskNotExistsError
        return task

    def delete_task(self, task: ToDo) -> None:
        self.session.delete(task)

    def get_all_tasks(self) -> list[ToDo]:
        return self.session.query(ToDo).all()
