from fastapi import APIRouter
from typing import List

from model.schema import Filme
from controller import ControladorFilme

movieRouter = APIRouter(
        prefix="/movie"
)


@movieRouter.get("/")
def root():
    return {"info": "Wydra Movie API"}


@movieRouter.get("/search")
def search_movie(query: str) -> List[Filme]:
    c = ControladorFilme()
    return c.get_by_titulo(query)


@movieRouter.get("/{id}")
def get_movie(id: int) -> Filme:
    c = ControladorFilme()
    return c.get(id)
