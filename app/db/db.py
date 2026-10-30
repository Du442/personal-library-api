from sqlmodel import SQLModel, Session, create_engine
from app.schemas.books import Book
from dotenv import load_dotenv
import os

load_dotenv()

path = os.getenv("DB_PATH")

engine = create_engine(f"sqlite:///{path}")