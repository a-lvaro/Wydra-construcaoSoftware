from typing import List
from fastapi import APIRouter

from core.config import Tags

from app.controllers import ControladorObra
from app.schemas import ObraNota

from core.database import get_session
from core.exceptions import NotFoundException

obraRouter = APIRouter(
    prefix="/obra"
)

@obraRouter.get(
    "/{id}",
    summary="Obter Obra",
    description="Obtem informações armazenadas sobre a obra.",
    tags=[Tags.obra]
)
def get_obra(id: int) -> ObraNota:
    with get_session() as db:
        controlador_obra = ControladorObra(db)

        obra = controlador_obra.get(id)

        if not obra:
            raise NotFoundException(detail="Obra não existe.")

        return ObraNota.from_orm(obra)