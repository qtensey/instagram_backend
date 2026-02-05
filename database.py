from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = 'postgresql+psycopg://tensey:1234@localhost:5432/instagram_db'

engine = create_engine(
    DATABASE_URL,
    echo = True,
    pool_size = 5,        # Скільки з'єднань тримати відкритими постійно (Base limit)
    max_overflow = 10,    # Скільки ДОДАТКОВИХ з'єднань можна створити, якщо всі 5 зайняті
    pool_timeout = 30,    # Скільки секунд чекати на вільне з'єднання перед тим, як впасти з помилкою
    pool_recycle=1800     # Перепідключати з'єднання кожні 30 хв (щоб база сама їх не вбила по таймауту)
)

# autocommit=False: Ми хочемо керувати транзакціями вручну (безпека).
# autoflush=False: Ми самі вирішуємо, коли синхронізувати дані.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass