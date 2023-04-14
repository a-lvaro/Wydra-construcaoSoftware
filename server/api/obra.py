from typing import List
from fastapi import APIRouter

from app.controllers import ControladorObra

from app.schemas import ObraNota

from core.database import get_session

obraRouter = APIRouter(
    prefix="/obra"
)

@obraRouter.get("/{id}")
def get_obra(id: int) -> ObraNota:
    with get_session() as db:
        controlador_obra = ControladorObra(db)
        obra = controlador_obra.get_or_create(id)

        return ObraNota.from_orm(obra)