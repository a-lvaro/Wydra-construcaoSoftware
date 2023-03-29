from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import logging

from api import userRouter
from api import estanteRouter

logging.basicConfig(level=logging.DEBUG)

wydra = FastAPI()

wydra.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

wydra.include_router(userRouter)
wydra.include_router(estanteRouter)


@wydra.get("/")
def root():
    return {"info": "Wydra API"}
