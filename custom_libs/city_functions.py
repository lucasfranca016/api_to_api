import requests
import redis
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def get_city_info(country: str):
    country = country.lower()
    cache_key = f"country:{country}"

    # Try to get data from cache
    cached = r.get(cache_key)

    if cached:
        print("Cache HIT")
        return json.loads(cached) # Converts info to dict, which allow it to be returned

    print("Cache MISS")
    
    cities_url = "https://countriesnow.space/api/v0.1/countries/cities"
    capital_url = "https://countriesnow.space/api/v0.1/countries/capital"

    response_cities = requests.post(cities_url, json={
        "country": country
    })
    
    response_capital = requests.post(capital_url, json={
        "country": country
    })
    
    info_cities = response_cities.json() # Transforms into a dict

    info_capital = response_capital.json() # Transforms into a dict
    
    try:
        cities = info_cities["data"] # Select the cities from the converted JSON
    
        capital = info_capital["data"]["capital"] # Select the capital from the converted JSON
        
        city_data = {
            "error": info_cities["error"],
            "msg": info_cities["msg"],
            "data": {
                "total_cities" : len(cities),
                "capital" : capital,
                "cities" : cities
        }}
        
    except KeyError:
        print('O país não foi encontrado')
    
        city_data = {
            "error": True,
            "msg": "country not found",
        }

    # Store the data in Redis using cache key. dumps() converts the dict into a string, since Redis stores data as strings
    r.set(cache_key, json.dumps(city_data), ex=300)
    
    return city_data