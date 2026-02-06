from database import Base
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, BigInteger, String, func, ForeignKey, Text, Boolean, Column, Table
from datetime import datetime

# --- Many-to-Many (Багато-до-Багатьох) ---
# Це проміжна таблиця, а не модель класу. 
# Вона потрібна лише для зв'язку Posts <-> Tags.
post_tag_association = Table(
    "post_tag",
    Base.metadata,
    # ondelete="CASCADE": Якщо видалити Post або Tag, то запис про зв'язок 
    # у цій таблиці видалиться автоматично самою базою даних. Це запобігає помилкам сміття.
    Column("post_id", ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
    # Обидва поля є primary_key=True, що створює "Складений первинний ключ".
    # Це гарантує, що не може бути дублікатів (один і той самий тег двічі на одному пості).
)

class User(Base):
    __tablename__ = "users"

    # BigInteger використовується для ID, якщо очікується дуже велика кількість юзерів.
    # Тип Mapped[int] — це підказка для Python, а BigInteger — тип для SQL.
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    
    # unique=True створює обмеження на рівні БД (ніхто не зареєструється з таким же email)
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    
    # default=True: працює на рівні Python (коли створюєш об'єкт User(..., is_active=True)).
    # Якщо потрібно, щоб БД сама ставила default, треба використовувати server_default.
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    
    # --- One-to-One (Один-до-Одного) ---
    # cascade="all, delete-orphan": Дуже важлива настройка!
    # Якщо ви видалите юзера (session.delete(user)), ORM автоматично видалить і його профіль.
    # delete-orphan - "Якщо дитина більше не пов'язана з цим батьком, її треба видалити з бази даних".
    profile: Mapped["Profile"] = relationship(back_populates="user", cascade="all, delete-orphan")
    
    # --- One-to-Many (Один-до-Багатьох) ---
    # Аналогічно, при видаленні юзера видаляться всі його пости.
    posts: Mapped[List["Post"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<User {self.username}>"

class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    
    # Mapped[str | None] — це сучасний синтаксис (Python 3.10+).
    # Означає, що поле може бути NULL у базі даних.
    bio: Mapped[str | None] = mapped_column(Text)
    avatar_url: Mapped[str | None] = mapped_column(String)
    
    # unique=True на ForeignKey — це саме те, що технічно перетворює 
    # зв'язок з One-to-Many на One-to-One. Один юзер може мати лише один профіль.
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), unique=True)
    
    # Тут немає List[], тому що профіль належить лише одному юзеру
    user: Mapped["User"] = relationship(back_populates="profile")

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str | None] = mapped_column(Text)
    
    # server_default=func.now(): 
    # Час встановлює база даних (PostgreSQL/MySQL) в момент INSERT, а не Python.
    # Це точніше і надійніше, ніж default=datetime.now.
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship(back_populates="posts")

    # --- Зв'язок Many-to-Many ---
    # secondary=post_tag_association вказує SQLAlchemy, через яку таблицю шукати теги.
    tags: Mapped[List["Tag"]] = relationship(
        secondary=post_tag_association,
        back_populates="posts"
    )

    def __repr__(self) -> str:
        return f"<Post(title={self.title})>"

class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)

    # Зворотний бік Many-to-Many.
    # Дозволяє отримати список постів по тегу: tag.posts
    posts: Mapped[List["Post"]] = relationship(
        secondary=post_tag_association,
        back_populates="tags"
    )

    def __repr__(self) -> str:
        return f"<Tag(name={self.name})>"