from sqlalchemy import select
from database import SessionLocal
from models import Post

with SessionLocal() as session:
    smtm = select(Post).where(Post.caption == "Red or Blue?")
    post_to_update = session.execute(smtm).scalar_one_or_none()

    if post_to_update:
        print(f"Old caption: {post_to_update.caption}")
        post_to_update.caption = "I choose the Red Pill!"
        session.commit()
        print("Caption updated!")