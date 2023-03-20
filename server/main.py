from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from routers import userRouter, movieRouter


wydra = FastAPI()

wydra.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

wydra.include_router(userRouter)
wydra.include_router(movieRouter)


@wydra.get("/")
def root():
    return {"info": "Wydra API"}
