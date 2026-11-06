from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    genre: str
    book_launch: date
    read: bool = False

class CreateBook(SQLModel):
    title: str
    author: str
    genre: str
    book_launch: date
    read: bool = False

class UpdateBook(SQLModel):
    title: str
    author: str
    genre: str
    book_launch: date
    read: bool = False