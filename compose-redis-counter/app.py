import os
from flask import Flask
from redis import Redis

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis')
redis = Redis(host=redis_host, port=6379)

@app.route('/')
def counter():
    hits = redis.incr('page_hits')
    return f"<h1>Счетчик посещений: {hits}</h1>\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)