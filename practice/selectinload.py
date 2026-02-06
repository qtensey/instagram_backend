from sqlalchemy import select
from sqlalchemy.orm import selectinload
from database import SessionLocal
from models import User

with SessionLocal() as session:
    
    # .options(selectinload(User.posts)) каже:
    # "Завантаж пости одразу, окремим ефективним запитом"
    stmt = (
        select(User)
        .options(selectinload(User.posts))
        .where(User.username == "neo_anderson")
    )

    user = session.execute(stmt).scalar_one_or_none()

    if user:
        print(f"User: {User.username}")
        for post in user.posts:
            print(f"- {post.caption}")