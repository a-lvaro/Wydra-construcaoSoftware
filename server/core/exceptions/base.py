from fastapi import HTTPException
from http import HTTPStatus


class CustomException(HTTPException):
    status_code = HTTPStatus.BAD_GATEWAY
    detail = HTTPStatus.BAD_GATEWAY.description

    def __init__(self, detail=None):
        if detail:
            self.detail = detail


class BadRequestException(CustomException):
    status_code = HTTPStatus.BAD_REQUEST
    detail = HTTPStatus.BAD_REQUEST.description


class NotFoundException(CustomException):
    status_code = HTTPStatus.NOT_FOUND
    detail = HTTPStatus.NOT_FOUND.description


class UnauthorizedException(CustomException):
    status_code = HTTPStatus.UNAUTHORIZED
    detail = HTTPStatus.UNAUTHORIZED.description

