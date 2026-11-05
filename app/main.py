from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.router import api_router

app = FastAPI(
    title="Personal Library API",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
async def health_check():
    return {"status": "OK"}