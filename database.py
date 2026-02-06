from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = 'postgresql+psycopg://tensey:1234@localhost:5432/instagram_db'

engine = create_engine(
    DATABASE_URL,
    pool_size = 5,
    max_overflow = 10,
    pool_pre_ping = True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass