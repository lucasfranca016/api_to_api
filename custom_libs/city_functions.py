import requests
from custom_libs.cache_functions import use_stored_cache
from custom_libs.cache_functions import store_cache

def get_city_info(country: str):
    country = country.lower()
    
    use_stored_cache(country)
    
    cache_key = use_stored_cache(country)
    
    if cache_key == f"country:{country}":
        cache_key = use_stored_cache(country)
    
    else: 
        cache_key = use_stored_cache(country)[0] # Get the cache_key result
    
    print(cache_key)
    
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
    store_cache(cache_key, city_data)
    
    return city_data