from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer


class ServicesContainer(DeclarativeContainer):
    frontend_url = providers.Dependency(instance_of=str)
