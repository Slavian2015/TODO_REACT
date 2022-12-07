import pytest
from src.api.todos.request import CreateTodoRequest


@pytest.mark.parametrize('title', [('qweasdzx:c',), ('123qweasd',), ('QQ',)])
def test_invalid_title_raise_error(title: str) -> None:
    with pytest.raises(ValueError):
        CreateTodoRequest(title=title)


def test_valid_title_returned() -> None:
    req = CreateTodoRequest(title="Title")
    assert req.title == 'Title'
