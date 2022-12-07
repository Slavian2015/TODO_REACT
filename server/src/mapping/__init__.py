# flake8: noqa

from sqlalchemy import MetaData


PublicMetadata = MetaData()

from src.mapping import todos


def perform_mapping() -> None:
    todos.perform_mapping()
