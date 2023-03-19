from fastapi import APIRouter, HTTPException

from model.schema import Filme
from controller import ControladorFilme

movieRouter = APIRouter(
        prefix="/movie"
)


@movieRouter.get("/{id}")
def get_movie(id: int) -> Filme:
    c = ControladorFilme()
    return c.get(id)
