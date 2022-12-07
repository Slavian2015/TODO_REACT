from typing import Optional
from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from src.api.error_handlers import DomainError
from src.handlers.interface import QueryHandlerInterface
from src.repositories.errors import TaskNotExistsError
from src.repositories.interface import TodosRepositoryInterface
from src.api.todos.response import GetTodoListResponse
from src.api.todos.response import GetTodoDetailsResponse
from src.query.todos import GetTodoQuery


class GetTaskQueryHandler(QueryHandlerInterface):
    def __init__(self, todos_repository: TodosRepositoryInterface) -> None:
        self.todos_repository = todos_repository

    def handle(self, query: GetTodoQuery) -> GetTodoDetailsResponse:
        with self.todos_repository.autocommit():
            try:
                task = self.todos_repository.get_task_by_id(query.task_id)
                found_data = GetTodoDetailsResponse.from_data(task)
            except SQLAlchemyError:
                raise DomainError('Failed to get task information')
            except TaskNotExistsError as e:
                raise DomainError(str(e))
        return found_data


class GetTasksListQueryHandler(QueryHandlerInterface):
    def __init__(self, todos_repository: TodosRepositoryInterface) -> None:
        self.todos_repository = todos_repository

    def handle(self, query: Optional[Any]) -> GetTodoListResponse:
        with self.todos_repository.autocommit():
            try:
                tasks = self.todos_repository.get_all_tasks()
                found_data = GetTodoListResponse.from_data(tasks)
            except SQLAlchemyError:
                raise DomainError('Failed to get tasks information')
        return found_data
