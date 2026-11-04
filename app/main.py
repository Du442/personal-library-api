from fastapi import FastAPI
from contextlib import asynccontextmanager

app = FastAPI(
    title="Personal Library API",
    version="1.0.0"
)

@app.get("/")
async def health_check():
    return {"status": "OK"}