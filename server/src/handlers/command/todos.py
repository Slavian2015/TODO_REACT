from sqlalchemy.exc import SQLAlchemyError

from src.api.error_handlers import DomainError
from src.api.todos.response import GetTodoDetailsResponse
from src.command.todos import DeleteTodoCommand
from src.command.todos import UpdateTodoCommand
from src.command.todos import CreateTodoCommand
from src.domain.todos import ToDo
from src.handlers.interface import CommandHandlerInterface
from src.repositories.errors import TaskExistsError
from src.repositories.errors import TaskNotExistsError
from src.repositories.interface import TodosRepositoryInterface
from src.value_object.value_object import TodoTitle


class CreateTaskCommandHandler(CommandHandlerInterface):
    def __init__(self, todos_repository: TodosRepositoryInterface) -> None:
        self.todos_repository = todos_repository

    def handle(self, command: CreateTodoCommand) -> GetTodoDetailsResponse:
        with self.todos_repository.autocommit():
            try:
                task = self.create_task(command)
                response = GetTodoDetailsResponse.from_data(task)
            except SQLAlchemyError:
                raise DomainError('Failed to create task')
            except TaskExistsError:
                raise DomainError('Task already exists')
        return response

    def create_task(self, command: CreateTodoCommand) -> ToDo:
        task = ToDo(title=TodoTitle(command.title))
        self.todos_repository.create_task(task)
        return task


class UpdateTaskCommandHandler(CommandHandlerInterface):
    def __init__(self, todos_repository: TodosRepositoryInterface) -> None:
        self.todos_repository = todos_repository

    def handle(self, command: UpdateTodoCommand) -> None:
        with self.todos_repository.autocommit():
            try:
                task = self.todos_repository.get_task_by_id(command.task_id)
                task.update_todo(TodoTitle(command.title))
            except SQLAlchemyError:
                raise DomainError('Failed to update task')
            except TaskNotExistsError as e:
                raise DomainError(str(e))


class DeleteTaskCommandHandler(CommandHandlerInterface):
    def __init__(self, todos_repository: TodosRepositoryInterface) -> None:
        self.todos_repository = todos_repository

    def handle(self, command: DeleteTodoCommand) -> None:
        with self.todos_repository.autocommit():
            try:
                task = self.todos_repository.get_task_by_id(command.task_id)
                self.todos_repository.delete_task(task)
            except SQLAlchemyError:
                raise DomainError('Failed to delete task')
            except TaskNotExistsError as e:
                raise DomainError(str(e))
