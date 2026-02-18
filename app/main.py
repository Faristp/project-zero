from fastapi import FastAPI
from app.routes import item

app = FastAPI()

app.include_router(item.router)

@app.get("/")
async def root():
    return {" Hello world from fastAPI Application"}