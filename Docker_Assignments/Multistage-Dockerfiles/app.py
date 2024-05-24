from flask import Flask
import redis

app=Flask(__name__)
cache=redis.redis(host='redis', port=6379)

@app.route('/')
def hello():
    try:
        hits=cache.incr('hits')
        return 'Hello World! I have been seen {} times.'.format(hits)
    except redis.exceptions.ConnectionError:
        return "Error: Cannot connect to Redis, counter disabled."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)