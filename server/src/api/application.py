from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

import src
from src.api.error_handlers import DomainError
from src.api.error_handlers import http409_error_handler
import src.api.todos.router as todos_endpoints
from src.container import AppContainer
from src.mapping import perform_mapping

BASE_PATH = Path(__file__).parent.parent.parent.absolute()
load_dotenv(BASE_PATH / '.env')

container = AppContainer()

container.config.sqlite_dsn.from_env('POSTGRESQL_DSN')

container.config.base_dir.from_value(BASE_PATH)
container.config.frontend_base_url.from_env('FRONTEND_BASE_URL', default='')


container.wire(packages=[src])
perform_mapping()

api = FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_origins=['0.0.0.0', '*', 'localhost'],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)


@api.on_event('startup')
def startup() -> None:
    container.init_resources()


@api.on_event('shutdown')
def shutdown() -> None:
    container.shutdown_resources()


api.add_exception_handler(DomainError, http409_error_handler)
api.include_router(todos_endpoints.router, tags=['todos'])
