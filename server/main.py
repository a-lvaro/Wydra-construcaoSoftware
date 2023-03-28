from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from api import userRouter

wydra = FastAPI()

wydra.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

wydra.include_router(userRouter)


@wydra.get("/")
def root():
    return {"info": "Wydra API"}
