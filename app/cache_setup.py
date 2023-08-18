import pickle
import redis

from . import settings

def redis_cache():
    return redis.from_url(settings.REDIS_HOST_URL)

def set_cache(key:str, data_to_cache:...):
    redis_cache.set(key, pickle.dumps(data_to_cache))
