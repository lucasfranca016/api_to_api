import redis
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def use_stored_cache(country):
    cache_key = f"country: {country}"

    # Try to get data from cache
    cached = r.get(cache_key)

    if cached:
        print("Cache HIT")
        return cache_key, json.loads(cached) # Converts info to dict, which allow it to be returned
    
    print("Cache MISS")
    return cache_key, None
    
def store_cache(cache_key, city_data):
    r.set(cache_key, json.dumps(city_data), ex=300)