from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select

from app.db.db import get_session
from app.repositories.book_repository import BookRepository
from app.schemas.books import Book

# ---------------------------------------------------------
# 1. Injeção do Repositório
# ---------------------------------------------------------
def get_book_repository(session: Session = Depends(get_session)) -> BookRepository:
    """Instancia o repositório injetando a sessão da base de dados."""
    return BookRepository(session)

# Criamos um "Alias" (atalho) limpo para usar nas rotas
BookRepoDep = Annotated[BookRepository, Depends(get_book_repository)]


# ---------------------------------------------------------
# 2. Injeção de Validação / Regras de Negócio
# ---------------------------------------------------------
def verify_book_exists(book_id: int, session: Session = Depends(get_session)) -> Book:
    """
    Verifica se um livro existe pelo ID.
    Se não existir, lança um erro 404. Se existir, devolve o livro.
    """
    book = session.exec(select(Book).where(Book.id == book_id)).first()
    
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"O livro com o ID {book_id} não foi encontrado."
        )
    return book

# Alias para quando precisarmos do livro já validado na rota
ValidBookDep = Annotated[Book, Depends(verify_book_exists)]