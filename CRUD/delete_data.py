from sqlalchemy import select
from database import SessionLocal
from models import Post

with SessionLocal() as session:
    smtm_del = select(Post).where(Post.image_url == "rabbit.jpg")
    post_to_delete = session.execute(smtm_del).scalar_one_or_none()

    if post_to_delete:
        session.delete(post_to_delete)
        session.commit()
        print("post deleted!")