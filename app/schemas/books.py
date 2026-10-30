from sqlmodel import SQLModel, Field
from datetime import date

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    author: str
    genre: str
    book_launch: date
    read: bool