import os
import time
from flask import Flask
import redis

app = Flask(__name__)

# Забираем параметры из переменных окружения (если их нет — берем дефолты)
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

# Подключаемся с повторными попытками (на случай, если база еще не успела стартовать)
def get_redis_connection():
    retries = 5
    while True:
        try:
            return redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(1)

r = get_redis_connection()

@app.route('/')
def hello():
    # Инкрементируем счетчик в базе Redis
    count = r.incr('hits')
    return f"""
    <div style="text-align: center; font-family: sans-serif; margin-top: 50px;">
        <h1>🚀 DevOps Lab 02: Persistence & Networks</h1>
        <p>Этот счетчик хранится в Redis с постоянным томом (Volume):</p>
        <h2 style="color: #2ecc71; font-size: 48px;">{count}</h2>
        <p>Попробуй перезапустить контейнеры — число не сбросится!</p>
    </div>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)