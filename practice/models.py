from typing import List, Optional # Потрібно для типізації списків
from sqlalchemy import String, func, BigInteger, ForeignKey, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "instagram_users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    # alembic: added bio field to user class
    # bio: Mapped[Optional[str]] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), server_default=text("'new'"))

    posts: Mapped[List["Post"]] = relationship(back_populates="user", cascade="all, delete-orphan")


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    image_url: Mapped[str] = mapped_column(Text, nullable=False)
    caption: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    user_id: Mapped[int] = mapped_column(ForeignKey("instagram_users.id", ondelete="CASCADE"))

    user: Mapped["User"] = relationship(back_populates="posts")