import redis
import json
from django.conf import settings

def get_redis_connection():
    return redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

def subscribe_to_course_updates():
    redis_conn = get_redis_connection()
    pubsub = redis_conn.pubsub()
    pubsub.subscribe('course_updates')

    print('Listening for course updates...')
    for message in pubsub.listen():
        if message['type'] == 'message':
            handle_course_update(json.loads(message['data']))

def handle_course_update(message):
    print(f"Received course update: {message}")
