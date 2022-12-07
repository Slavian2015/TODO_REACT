from __future__ import annotations

from abc import abstractmethod
from types import TracebackType
from typing import Any
from typing import Optional
from typing import Protocol
from typing import Type
from uuid import UUID

from src.domain.todos import ToDo


class AutocommitInterface(Protocol):
    @abstractmethod
    def autocommit(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    def __enter__(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> bool:
        raise NotImplementedError


class TodosRepositoryInterface(AutocommitInterface):

    @abstractmethod
    def create_task(self, todos: ToDo) -> UUID:
        raise NotImplementedError

    @abstractmethod
    def get_task_by_id(self, task_id: UUID) -> ToDo:
        raise NotImplementedError

    @abstractmethod
    def get_all_tasks(self) -> list[ToDo]:
        raise NotImplementedError

    @abstractmethod
    def delete_task(self, task: ToDo) -> None:
        raise NotImplementedError
