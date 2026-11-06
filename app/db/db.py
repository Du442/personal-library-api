from sqlmodel import SQLModel, Session, create_engine
from typing import Generator
from dotenv import load_dotenv
import os

load_dotenv()

path = os.getenv("DB_PATH", "database.db")
db_url = path if path.startswith("sqlite") else f"sqlite:///{path}"
connect_args = {"check_same_thread": False} if db_url.startswith("sqlite") else {}

engine = create_engine(db_url, echo=True, connect_args=connect_args)

def init_db() -> None:
    
    # Importe os modelos
    from app.schemas.books import Book

    # Cria as tabelas
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session