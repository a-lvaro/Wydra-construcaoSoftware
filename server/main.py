from fastapi import FastAPI

wydra = FastAPI()

@wydra.get("/")
async def root():
    return {"info": "Wydra API"}
