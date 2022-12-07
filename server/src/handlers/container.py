from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from src.handlers.command.todos import CreateTaskCommandHandler
from src.handlers.command.todos import UpdateTaskCommandHandler
from src.handlers.command.todos import DeleteTaskCommandHandler
from src.handlers.query.todos import GetTaskQueryHandler
from src.handlers.query.todos import GetTasksListQueryHandler


class HandlersContainer(DeclarativeContainer):
    repositories = providers.DependenciesContainer()
    services = providers.DependenciesContainer()

    create_task = providers.Factory(CreateTaskCommandHandler, todos_repository=repositories.todos)
    update_task = providers.Factory(UpdateTaskCommandHandler, todos_repository=repositories.todos)
    get_task = providers.Factory(GetTaskQueryHandler, todos_repository=repositories.todos)
    delete_task = providers.Factory(DeleteTaskCommandHandler, todos_repository=repositories.todos)
    get_tasks_list = providers.Factory(GetTasksListQueryHandler, todos_repository=repositories.todos)
