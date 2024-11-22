from sqlmodel import Session, SQLModel, create_engine
from .config import get_settings
from .models import *

settings = get_settings()

DATABASE_URL = (
    f"postgresql://{settings.postgres_user}:{settings.postgres_password}"
    f"@db/{settings.postgres_db}"
)

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_db():
    with Session(engine) as session:
        yield session
        

