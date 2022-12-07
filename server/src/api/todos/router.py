from uuid import UUID

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from starlette import status

from src.api.todos.request import CreateTodoRequest
from src.api.todos.request import UpdateTodoRequest
from src.api.todos.response import GetTodoDetailsResponse
from src.api.todos.response import GetTodoListResponse
from src.api.todos.response import UpdateTodoResponse
from src.command.todos import CreateTodoCommand
from src.command.todos import UpdateTodoCommand
from src.command.todos import DeleteTodoCommand
from src.query.todos import GetTodoQuery
from src.container import AppContainer
from src.handlers.interface import CommandHandlerInterface
from src.handlers.interface import QueryHandlerInterface
from src.repositories.errors import PersistenceError

router = APIRouter()


@router.get('/todos', response_model=GetTodoListResponse)
@inject
def get_all_tasks(
        handler: CommandHandlerInterface[None, GetTodoListResponse] =
        Depends(Provide[AppContainer.handlers.get_tasks_list])
) -> GetTodoListResponse:
    try:
        tasks_list = handler.handle(None)
    except PersistenceError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return tasks_list


@router.post('/todos', response_model=GetTodoDetailsResponse)
@inject
def create_task(
        request: CreateTodoRequest,
        handler: CommandHandlerInterface[CreateTodoCommand, GetTodoDetailsResponse] =
        Depends(Provide[AppContainer.handlers.create_task])
) -> GetTodoDetailsResponse:
    try:
        task_data = handler.handle(CreateTodoCommand(title=request.title))
    except PersistenceError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return task_data


@router.patch('/todos/{task_id}', response_model=UpdateTodoResponse)
@inject
def update_task(
        task_id: UUID,
        request: UpdateTodoRequest,
        handler: CommandHandlerInterface[UpdateTodoCommand, None] =
        Depends(Provide[AppContainer.handlers.update_task])
) -> UpdateTodoResponse:
    try:
        handler.handle(UpdateTodoCommand(title=request.title, task_id=task_id))
    except PersistenceError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return UpdateTodoResponse()


@router.get('/todos/{task_id}', response_model=GetTodoDetailsResponse)
@inject
def get_task(
        task_id: UUID,
        handler: QueryHandlerInterface[GetTodoQuery, GetTodoDetailsResponse] =
        Depends(Provide[AppContainer.handlers.get_task])
) -> GetTodoDetailsResponse:
    try:
        task_data = handler.handle(GetTodoQuery(task_id=task_id))
    except PersistenceError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return task_data


@router.delete('/todos/{task_id}', response_model=UpdateTodoResponse)
@inject
def delete_task(
        task_id: UUID,
        handler: QueryHandlerInterface[DeleteTodoCommand, None] =
        Depends(Provide[AppContainer.handlers.delete_task])
) -> UpdateTodoResponse:
    try:
        handler.handle(DeleteTodoCommand(task_id=task_id))
    except PersistenceError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return UpdateTodoResponse()
