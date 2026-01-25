from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_engine('postgresql+psycopg://postgres:password@localhost:5432/insta_db')

class Basse(DeclarativeBase):
    pass