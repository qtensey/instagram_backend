from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column()
    username: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    is_active: Mapped[bool] = mapped_column()

class Profile(Base):
    __tablename__ = "profiles"

    id
    user_id
    bio
    avatar_url

class Post(Base):
    __tablename__ = "posts"

    id
    user_id
    title
    content
    created_at

class Tag(Base):
    __tablename__ = "tags"

    id
    name

class PostTags(Base):
    post_id
    tag_id