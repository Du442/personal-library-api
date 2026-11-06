from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from app.schemas.books import Book, CreateBook, UpdateBook
from app.repositories.book_repository import BookRepository
from app.dependencies import BookRepoDep, ValidBookDep

router = APIRouter()

@router.get("/", response_model=list[Book])
def list_books(books_repo: BookRepoDep):
    return books_repo.read_books()

@router.get("/{book_id}", response_model=Book | None)
def read_book(books_repo: BookRepoDep,
                    book_id: int):
    book = books_repo.read_book(book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book

@router.post("/", response_model=Book, status_code=201)
def create_book(books_repo: BookRepoDep,
                        info: CreateBook):
    return books_repo.create_book(info)

@router.put("/{book_id}", response_model=Book | None)
def update_book(books_repo: BookRepoDep,
                        book_id: int,
                        book: UpdateBook):
    
    book = books_repo.update_book(book, book_id)

    if not book:
        raise HTTPException(404, "Book not found")

    return book

@router.delete("/{book_id}", status_code=204)
def delete_book(books_repo: BookRepoDep,
                        book_id: int):

    book = books_repo.delete_book(book_id)

    if not book:
        raise HTTPException(404, "Not found")

    return book