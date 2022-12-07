from typing import Callable
from typing import Any
from typing import Generator

from faker import Faker
from starlette.testclient import TestClient

from src.api.application import api

import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from src.api.application import container

from src.domain.todos import ToDo

from src.value_object.value_object import TodoTitle


@pytest.fixture(scope='module')
def app_container() -> Generator:
    yield container


@pytest.fixture
def api_client() -> TestClient:
    return TestClient(api)


@pytest.fixture
def session_factory() -> Callable[..., Session]:
    return sessionmaker(bind=container.sqlalchemy_engine())


@pytest.fixture
def task_factory(faker: Faker) -> Callable[..., ToDo]:
    def maker(**kwargs: Any) -> ToDo:
        task = ToDo(title=TodoTitle(faker.word()))
        return task
    return maker
