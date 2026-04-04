import requests
from custom_libs.cache_functions import use_stored_cache
from custom_libs.cache_functions import store_cache

def get_country_info(country_name):
    country_name = country_name.lower()
    
    cache_key, cached_data = use_stored_cache(country_name)
    
    if cached_data:
        return cached_data

    api_url = "https://countriesnow.space/api/v0.1/countries"

    country_payload = {
        "country": country_name
    }

    response_population = requests.post(
        url = api_url + "/population",
        data = country_payload
    )

    # TODO: Make the remaining requests and combine the results
    
    store_cache(cache_key, response_population.json())
    
    return response_population.json()