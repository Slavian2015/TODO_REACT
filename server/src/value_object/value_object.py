import re


class TodoTitle:
    def __init__(self, title: str) -> None:
        valid_name = r"^[a-zA-Z0-9-( )_]*$"
        valid_first_character = r"^[a-zA-Z]*$"
        if not title:
            raise ValueError('Invalid post name')

        if not re.match(valid_name, title):
            raise ValueError('Invalid post title.'
                             'Valid post name can only contain alphanumeric characters and underscores')
        if not re.match(valid_first_character, title[0]):
            raise ValueError('Invalid post title. '
                             'The first character of valid post title must be an alphabetic character')
        self._title = title

    def __str__(self) -> str:
        return self._title
