from fastapi import FastAPI

from routers import userRouter

wydra = FastAPI()

wydra.include_router(userRouter)


@wydra.get("/")
def root():
    return {"info": "Wydra API"}
