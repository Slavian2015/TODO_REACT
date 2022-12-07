class RepositoryError(RuntimeError):
    message: str = ''

    def __init__(self) -> None:
        super().__init__(self.message)


class PersistenceError(RuntimeError):
    pass


class TaskExistsError(RuntimeError):
    pass


class TaskNotExistsError(RepositoryError):
    message = 'Task not found'
