from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from sqlalchemy.orm.scoping import ScopedSession

from src.repositories.todos import TodosRepository


class RepositoriesContainer(DeclarativeContainer):
    sqlalchemy_session = providers.Dependency(instance_of=ScopedSession)

    todos = providers.Factory(TodosRepository, session=sqlalchemy_session)
