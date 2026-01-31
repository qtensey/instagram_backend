from sqlalchemy import select
from sqlalchemy.orm import joinedload
from database import engine, Base, SessionLocal
from models import User, Post

# Ця команда створює всі таблиці, які знайшла в Base
# Вона еквівалентна CREATE TABLE IF NOT EXISTS
print("Creating tables...")
# Base.metadata.create_all(bind=engine)
print("Tables created successfully!")

with SessionLocal() as session:
    new_user = User(
        username = "Darth Vader",
        email = "DarthVader@gmail.com",
        posts = [
            Post(image_url = "DarthVader.jpg", caption = "Come to the dark side")
        ]
    )
    session.add(new_user)
    session.commit()

    stmt = (
        select(Post)
        .options(joinedload(Post.user))
        .where(Post.caption == "Come to the dark side")
    )
    post = session.execute(stmt).scalar_one_or_none()
    
    if post:
        print(f"Post: {post.caption}")
        print(f"Author: {post.user.username} (email: {post.user.email})")
    else:
        print("Post not found")

    if post:
        print(f"Old caption: {post.caption}")
        post.caption = "We have coockies"
        session.commit()
        print(f"New caption: {post.caption}")

    stmt_del = select(Post).where(Post.image_url == "DarthVader.jpg")
    post_to_delete = session.execute(stmt_del).scalar_one_or_none()
    
    if post_to_delete:
        session.delete(post_to_delete)
        session.commit()
        print("Post deleted")