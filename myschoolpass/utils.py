import redis
import json
from django.conf import settings

def get_redis_connection():
    return redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

def publish_course_update(course):
    redis_conn = get_redis_connection()
    message = {
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'level': course.level,
        'available_seats': course.available_seats,
        'expiration_date': str(course.expiration_date),
    }
    redis_conn.publish('course_updates', json.dumps(message))
