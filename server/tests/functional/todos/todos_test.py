from typing import Callable

from faker import Faker
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker

from src.domain.todos import ToDo


def test_create_new_task(
        session_factory: sessionmaker,
        api_client: TestClient,
        faker: Faker
) -> None:
    with session_factory() as s:
        payload: dict = {"title": faker.word()}

        response = api_client.post('/todos', json=payload)

        assert response.status_code == 200
        json = response.json()
        assert 'id' in json.keys()
        task = s.query(ToDo).get(json['id'])
        assert task is not None
        assert task.title == payload["title"]
        list(map(s.delete, [task]))
        s.commit()


def test_update_task(
        session_factory: sessionmaker,
        api_client: TestClient,
        task_factory: Callable[..., ToDo],
        faker: Faker
) -> None:
    with session_factory() as s:
        task = task_factory()
        s.add(task)
        s.commit()

        payload: dict = {"title": faker.word()}
        response = api_client.patch(f'/todos/{task.id}', json=payload)

        assert response.status_code == 200
        s.refresh(task)

        assert task.title == payload["title"]
        list(map(s.delete, [task]))
        s.commit()


def test_delete_task(
        session_factory: sessionmaker,
        api_client: TestClient,
        task_factory: Callable[..., ToDo],
        faker: Faker
) -> None:
    with session_factory() as s:
        task = task_factory()
        s.add(task)
        s.commit()

        task_id = task.id
        response = api_client.delete(f'/todos/{task.id}')
        assert response.status_code == 200

    with session_factory() as s:
        task_from_db = s.query(ToDo).get(task_id)
        assert task_from_db is None


def test_get_list_of_tasks(
        session_factory: sessionmaker,
        api_client: TestClient,
        task_factory: Callable[..., ToDo],
        faker: Faker
) -> None:
    with session_factory() as s:
        task = task_factory()
        task2 = task_factory()
        task3 = task_factory()
        s.add_all([task, task2, task3])
        s.commit()

        response = api_client.get('/todos')

        assert response.status_code == 200

        uploaded_data = response.json()

        assert len(uploaded_data['tasks']) == 3
        list(map(s.delete, [task, task2, task3]))
        s.commit()
