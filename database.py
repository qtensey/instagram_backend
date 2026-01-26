from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine('postgresql+psycopg://tensey:1234@localhost:5432/instagram_db')

# autocommit=False: Ми хочемо керувати транзакціями вручну (безпека).
# autoflush=False: Ми самі вирішуємо, коли синхронізувати дані.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass