from sqlalchemy import select
from database import engine, Base, SessionLocal
from models import User, Post

# Ця команда створює всі таблиці, які знайшла в Base
# Вона еквівалентна CREATE TABLE IF NOT EXISTS
print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")

with SessionLocal() as session:
    new_user = User(
        username="neo_anderson",
        email="neo@matrix.com",
        posts=[
            Post(image_url="rabbit.jpg", caption="Follow the white rabbit"),
            Post(image_url="pill.jpg", caption="Red or Blue?")
        ]
    )

    session.add(new_user)
    session.commit()
    print("Data safety!")

with SessionLocal() as session:
    smtm = select(Post).where(Post.caption == "Red or Blue?")
    post_to_update = session.execute(smtm).scalar_one_or_none()

    if post_to_update:
        print(f"Old caption: {post_to_update.caption}")
        post_to_update.caption = "I choose the Red Pill!"
        session.commit()
        print("Caption updated!")

with SessionLocal() as session:
    smtm_del = select(Post).where(Post.image_url == "rabbit.jpg")
    post_to_delete = session.execute(smtm_del).scalar_one_or_none()

    if post_to_delete:
        session.delete(post_to_delete)
        session.commit()
        print("post deleted!")