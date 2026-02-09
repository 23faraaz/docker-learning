import os
from flask import Flask
import redis

# Create Flask app
app = Flask(__name__)

# Read Redis connection details from environment variables
# If they don't exist, use safe defaults
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))

# Create Redis client
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def welcome():
    return "Welcome to the CoderCo Containers Challenge"

@app.route('/count')
def count():
    visits = r.incr("visits")
    return f"Total visits: {visits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
