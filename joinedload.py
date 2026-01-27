from sqlalchemy import select
from sqlalchemy.orm import joinedload
from database import SessionLocal
from models import Post

with SessionLocal() as session:
    # SCENARIO: Ми хочемо знайти пост і ОДРАЗУ його автора.
    # joinedload(Post.user) каже: "Зроби JOIN з таблицею users"
    stmt = (
        select(Post)
        .options(joinedload(Post.user))
        .where(Post.caption == "Follow the white rabbit")
    )
    post = session.execute(stmt).scalar_one_or_none()

    if post:
        print(f"Post: {post.caption}")
        print(f"Author: {post.user.username} (Email: {post.user.email})")
    else:
        print("Post not found")