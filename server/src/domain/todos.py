import uuid
from datetime import datetime
from typing import Optional

from src.value_object.value_object import TodoTitle


class ToDo:
    def __init__(self, title: TodoTitle) -> None:
        self.id = uuid.uuid4()
        self.title = str(title)
        self.date_created = datetime.now()
        self.date_updated: Optional[datetime] = None

    def update_todo(self, title: TodoTitle) -> None:
        self.date_created = datetime.now()
        self.title = str(title)
