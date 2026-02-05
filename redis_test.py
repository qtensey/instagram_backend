import redis
import time

import redis
import time

# 1. Підключення (Redis зазвичай висить на порту 6379)
# decode_responses=True означає, що ми отримуємо str, а не bytes
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

print("--- Basic String ---")
# SET key value
r.set('user:neo:role', 'The One')
# GET key
role = r.get('user:neo:role')
print(f"Neo is: {role}")

print("\n--- TTL (Time To Live) ---")
# Зберегти ключ, який живе 3 секунди
r.set('self_destruct', 'Boom!', ex=3) 
print(f"Message: {r.get('self_destruct')}")
print("Sleeping 4 seconds...")
time.sleep(4)
print(f"Message after sleep: {r.get('self_destruct')}") # Має бути None

print("\n--- Lists (Queues) ---")
# Push в список
r.lpush('tasks', 'clean_room')
r.lpush('tasks', 'learn_python')
# Pop (дістати) зі списку
task = r.rpop('tasks')
print(f"Doing task: {task}")