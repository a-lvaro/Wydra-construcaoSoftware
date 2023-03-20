from fastapi import FastAPI

from routers import userRouter, movieRouter

wydra = FastAPI()

wydra.include_router(userRouter)
wydra.include_router(movieRouter)


@wydra.get("/")
def root():
    return {"info": "Wydra API"}
