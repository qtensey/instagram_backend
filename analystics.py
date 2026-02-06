import sys
import time
from sqlalchemy import select
from sqlalchemy.orm import selectinload
# Увімкнемо echo=True тимчасово для цього скрипта, щоб бачити SQL в консолі
from database import SessionLocal, engine 

# Цей хак змушує engine писати логи, навіть якщо в database.py стоїть echo=False
engine.echo = True

def get_feed_bad():
    """
    Поганий підхід (Lazy Loading).
    Ми просто беремо юзерів, а пости і теги SQLAlchemy підтягує "на льоту".
    """
    print("\n" + "="*50)
    print("STARTING BAD QUERY (N+1 Problem)")
    print("="*50)
    
    with SessionLocal() as session:
        start_time = time.time()
        
        # 1. Запит тільки за юзерами
        users = session.scalars(select(User)).all()
        
        for user in users:
            print(f"\nUser: {user.username}")
            # ТУТ починається пекло:
            # user.posts робить окремий SQL-запит для кожного юзера
            for post in user.posts:
                # post.tags робить ЩЕ ОДИН запит для КОЖНОГО поста
                tag_names = [t.name for t in post.tags]
                print(f"  - Post: {post.title} | Tags: {tag_names}")
                
        end_time = time.time()
        print(f"\n❌ BAD Execution time: {end_time - start_time:.4f} seconds")

def get_feed_optimized():
    """
    Хороший підхід (Eager Loading).
    Ми кажемо базі: "Дай все й одразу".
    """
    print("\n" + "="*50)
    print("✅ STARTING OPTIMIZED QUERY")
    print("="*50)
    
    with SessionLocal() as session:
        start_time = time.time()
        
        # МАГІЯ ТУТ:
        # Ми будуємо ланцюжок завантаження:
        # 1. Завантаж User.posts (selectinload)
        # 2. Всередині posts завантаж Post.tags (selectinload)
        stmt = (
            select(User)
            .options(
                selectinload(User.posts).selectinload(Post.tags)
            )
        )
        
        users = session.scalars(stmt).all()
        
        # Тепер дані вже в пам'яті, Python просто читає їх миттєво
        for user in users:
            print(f"\nUser: {user.username}")
            for post in user.posts:
                tag_names = [t.name for t in post.tags]
                print(f"  - Post: {post.title} | Tags: {tag_names}")

        end_time = time.time()
        print(f"\n✨ OPTIMIZED Execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    # Імпорт моделей тут, щоб уникнути циклічних імпортів, якщо вони є
    from models import User, Post
    
    # Спочатку запускаємо поганий варіант
    get_feed_bad()
    
    # Робимо паузу, щоб візуально відділити логи
    print("\n\n" + "*"*50 + "\n\n")
    
    # Запускаємо хороший варіант
    get_feed_optimized()