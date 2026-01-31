from database import SessionLocal
from models import User
from sqlalchemy import select


with SessionLocal() as session:
    stmt = select(User).where(User.username == "neo_anderson")

    # .scalar_one_or_none() — це метод, який каже: 
    # "Я очікую рівно один результат або нічого. Якщо буде 2 юзера — впади з помилкою".
    user = session.execute(stmt).scalar_one_or_none()

    if user:
        print(f"User found: {user.username}, Email: {user.email}")

        for post in user.posts:
            print(f"- Post: {post.caption} (Image: {post.image_url})")
    else:
        print("User not found")