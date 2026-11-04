from fastapi import Depends
from typing import Annotated

from app.db.db import DBLocal
from app.repositories.book_repository import BookRepository

db = DBLocal()

def catch_db() -> DBLocal:
    return db

def catch_book_repository(
        db_local: Annotated[DBLocal,
                            Depends(catch_db)]
) -> BookRepository:
    return BookRepository(db_local)