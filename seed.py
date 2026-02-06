import random
from models import User, Post, Profile, Tag
from database import SessionLocal

with SessionLocal() as session:
    tag_python = Tag(name="python")
    tag_life = Tag(name="life")
    tag_coding = Tag(name="coding")
    tag_travel = Tag(name="travel")
    tag_music = Tag(name="music")

    # Список всіх тегів, щоб брати випадкові
    all_tags = [tag_python, tag_life, tag_coding, tag_travel, tag_music]

    users_to_add = [
        User(
            username = "tensey", 
            email = "tensey26@gmail.com", 
            profile = Profile(bio = "learning python", avatar_url = "babbage.jpg"),
            posts = [
                # Передаємо список об'єктів тегів у параметр tags
                Post(title = "Kivertsi live 1", tags=[tag_life, tag_travel]),
                Post(title = "Kivertsi live 2", tags=[tag_travel]),
                Post(title = "Kivertsi live 3", tags=[tag_python, tag_coding]),
                Post(title = "Kivertsi live 4", tags=[tag_music]),
                Post(title = "Kivertsi live 5", tags=[tag_life, tag_music])
            ]
        ),
        User(
            username = "zozzy", 
            email = "zozzy12@gmail.com", 
            profile = Profile(bio = "learning python", avatar_url = "zozzy.jpg"),
            posts = [
                # Можна використовувати random.sample для автоматизації
                Post(title = "balabam 1", tags=random.sample(all_tags, 2)), 
                Post(title = "balabam 2", tags=[tag_coding]),
                Post(title = "balabam 3", tags=[tag_python]),
                Post(title = "balabam 4", tags=random.sample(all_tags, 3)),
                Post(title = "balabam 5", tags=[tag_life])
            ]
        ),
        User(
            username = "oxxy", 
            email = "oxxy20@gmail.com", 
            profile = Profile(bio = "learning python", avatar_url = "oxxy.jpg"),
            posts = [
                Post(title = "live in varash 1", tags=[tag_travel]),
                Post(title = "live in varash 2", tags=[tag_travel, tag_life]),
                Post(title = "live in varash 3", tags=[tag_coding]),
                Post(title = "live in varash 4", tags=[]), # Можна і без тегів
                Post(title = "live in varash 5", tags=[tag_python])
            ]
        ),
        User(
            username = "bobby", 
            email = "bobby@gmail.com", 
            profile = Profile(bio = "desire", avatar_url = "bobby.jpg"),
            posts = [
                Post(title = "desire 1", tags=[tag_travel]),
                Post(title = "desire 2", tags=[tag_travel, tag_life]),
                Post(title = "desire 3", tags=[tag_coding]),
                Post(title = "desire 4", tags=[]), # Можна і без тегів
                Post(title = "desire 5", tags=[tag_python])
            ]
        ),
        User(
            username = "biba", 
            email = "biba@gmail.com", 
            profile = Profile(bio = "learning python", avatar_url = "biba.jpg"),
            posts = [
                Post(title = "biba 1", tags=[tag_travel]),
                Post(title = "biba 2", tags=[tag_travel, tag_life]),
                Post(title = "biba 3", tags=[tag_coding]),
                Post(title = "biba 4", tags=[]), # Можна і без тегів
                Post(title = "biba 5", tags=[tag_python])
            ]
        ),
    ]

    # 2. Додаємо все в сесію
    # Достатньо додати тільки Юзерів. 
    # SQLAlchemy "каскадом" побачить, що у юзерів є пости, а у постів є теги, 
    # і збереже все автоматично.
    session.add_all(users_to_add)
    
    session.commit()
    print("Дані успішно додано!")