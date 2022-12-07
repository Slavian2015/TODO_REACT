from typing import Generator
from typing import Callable

from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from src.handlers.container import HandlersContainer
from src.repositories.container import RepositoriesContainer
from src.services.container import ServicesContainer


def database_engine(dsn: str) -> Generator:
    engine = create_engine(dsn)
    yield engine
    engine.dispose()


class AppContainer(DeclarativeContainer):
    config = providers.Configuration()
    sqlalchemy_engine = providers.Resource(database_engine, dsn=config.sqlite_dsn)
    maker: providers.Singleton = providers.Singleton(sessionmaker, bind=sqlalchemy_engine)
    scoped_session_provider: providers.Singleton[scoped_session] = providers.Singleton(
        scoped_session, session_factory=maker)
    sqlalchemy_session: providers.Singleton[Callable[..., Session]] = providers.Singleton(scoped_session_provider)

    repositories = providers.Container(RepositoriesContainer, sqlalchemy_session=sqlalchemy_session)
    services = providers.Container(ServicesContainer, frontend_url=config.frontend_base_url)

    handlers = providers.Container(HandlersContainer, repositories=repositories, services=services)
