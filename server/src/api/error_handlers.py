from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.requests import Request
from starlette.responses import JSONResponse


class DomainError(RuntimeError):
    pass


async def http409_error_handler(_: Request, exc: DomainError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content=jsonable_encoder({'detail': {'error': str(exc)}})
    )
