from database import engine, Base, SessionLocal
from models import User, Post

# Ця команда створює всі таблиці, які знайшла в Base
# Вона еквівалентна CREATE TABLE IF NOT EXISTS
print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")

with SessionLocal as session:
    

    session.commit()