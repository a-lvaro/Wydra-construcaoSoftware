from fastapi import FastAPI

wydra = FastAPI()

@wydra.get("/")
def root():
    return {"info": "Wydra API"}
