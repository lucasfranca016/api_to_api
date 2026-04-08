import requests
from requests import RequestException
from custom_libs.cache_functions import use_stored_cache
from custom_libs.cache_functions import store_cache
from tenacity import retry, stop_after_attempt, wait_exponential


@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=10))
def get_city_info(country: str):
    country = country.lower() # Avoid problems with capitalized country names
    
    cache_key, cached_data = use_stored_cache(country)
    
    if cached_data:
        return cached_data
    
    cities_url = "https://countriesnow.space/api/v0.1/countries/cities"
    capital_url = "https://countriesnow.space/api/v0.1/countries/capital"

    try:
        response_cities = requests.post(cities_url, json={
            "country": country
        })
        
        response_capital = requests.post(capital_url, json={
            "country": country
        })
        
        response_cities.raise_for_status()
        
        response_capital.raise_for_status()
        
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
            print('Country not found')
    
            city_data = {
                "error": True,
                "msg": "country not found",
            }

    except RequestException as error:
        print(f'Request error: {error}')
        raise
    
    # Store the data in Redis using cache key. dumps() converts the dict into a string, since Redis stores data as strings
    store_cache(cache_key, city_data)
    
    return city_data