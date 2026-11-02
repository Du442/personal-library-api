from fastapi import FastAPI
from app.db.db import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executado antes da aplicação começar a receber requisições
    init_db()
    yield

app = FastAPI(
    title="Personal Library API",
    version="1.0.0"
)

@app.get("/")
async def health_check():
    return {"status": "OK"}