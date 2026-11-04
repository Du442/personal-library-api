from typing import Sequence
from sqlmodel import Session, select
from app.schemas.books import Book, CreateBook, UpdateBook
from app.db.db import get_session
from fastapi import Depends

class BookRepository:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def create_book(self, book: CreateBook):
        book_create = Book.model_validate(book)
        self.session.add(book_create)
        self.session.commit()
        self.session.refresh(book_create)
        return book_create

    def update_book(self, book: UpdateBook, id: int):
        book_update = self.session.get(Book, id)
        book_data = book.model_dump(exclude_unset=True)
        book_update.sqlmodel_update(book_data)
        self.session.add(book_update)
        self.session.commit()
        self.session.refresh(book_update)
        return book_update

    def read_books(self):
        books = self.session.exec(select(Book).all())
        return books

    def read_book(self, id:int):
        book = self.session.get(Book, id)
        return book

    def delete_book(self, id:int):
        book = self.session.get(Book, id)
        self.session.delete(book)
        self.session.commit()
        return {"ok": True}