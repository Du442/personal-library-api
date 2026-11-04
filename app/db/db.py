from sqlmodel import SQLModel, Session, create_engine
from typing import Generator
from dotenv import load_dotenv
import os

load_dotenv()

path = os.getenv("DB_PATH")

connect_args = {"check_same_thread": False} if path.startswith("sqlite") else {}

engine = create_engine(f"{path}", echo=True, connect_args=connect_args)

class DBLocal:
    def __init__(self, engine):
        self.engine = engine

    def init_db(self) -> None:
        from app.schemas.books import Book, CreateBook, UpdateBook
        SQLModel.metadata.create_all(self.engine)

    def get_session(self) -> Generator[Session, None, None]:
        with Session(self.engine) as session:
            yield session