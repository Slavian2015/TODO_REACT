from __future__ import annotations


from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import DateTime

from src.domain.todos import ToDo
from src.mapping import PublicMetadata
from sqlalchemy.orm import registry

TodosTable = Table(
    'todos', PublicMetadata,
    Column('id', UUID(True), primary_key=True, index=True),
    Column('title', String(length=255), nullable=False),
    Column('date_created', DateTime, nullable=False),
    Column('date_updated', DateTime, nullable=True),
)


def perform_mapping() -> None:
    mapper_registry = registry()
    mapper_registry.map_imperatively(ToDo, TodosTable)
