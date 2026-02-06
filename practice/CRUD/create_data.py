import sys
import os

# Отримуємо шлях до папки, де лежить цей скрипт (CRUD)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Отримуємо батьківську папку (instagram_backend)
parent_dir = os.path.dirname(current_dir)
# Додаємо її в системні шляхи
sys.path.append(parent_dir)

from database import SessionLocal
from models import User, Post

with SessionLocal() as session:
    new_user = User(
        username="tensey",
        email="tensey26@gmail.com",
        # posts=[
        #    Post(image_url="rabbit.jpg", caption="Follow the white rabbit"),
        #    Post(image_url="pill.jpg", caption="Red or Blue?")
        # ]
    )

    session.add(new_user)
    session.commit()
    print("Data safety!")