from sqlmodel import SQLModel, Session, create_engine
from typing import Generator
from dotenv import load_dotenv
import os

load_dotenv()

path = os.getenv("DB_PATH")

connect_args = {"check_same_thread": False} if path.startswith("sqlite") else {}

engine = create_engine(f"{path}", echo=True, connect_args=connect_args)

def init_db() -> None:
    from app.schemas.books import Book, CreateBook, UpdateBook
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session