from database import SessionLocal
from models import User, Post

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