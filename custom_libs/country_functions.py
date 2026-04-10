import requests
from custom_libs.cache_functions import use_stored_cache
from custom_libs.cache_functions import store_cache
from tenacity import retry, stop_after_attempt, wait_exponential
from requests import RequestException
from custom_libs.retry_functions import should_retry

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=10))
def get_country_info(country_name):
    country_name = country_name.lower()
    
    cache_key, cached_data = use_stored_cache(country_name)
    
    if cached_data:
        return cached_data

    api_url = "https://countriesnow.space/api/v0.1/countries"

    country_payload = {
        "country": country_name
    }

    try:
        response_population = requests.post(
            url = api_url + "/population",
            data = country_payload
        )
        
        response_population.raise_for_status()
        
        should_retry(response_population)

        # TODO: Make the remaining requests and combine the results
        
    except RequestException as error:
        if error.response is not None:
            print(f'HTTP error: {error.response.status_code}')
            return {
            "error": True,
            "msg": f"HTTP error {error.response.status_code}"
            }
        raise
        
    store_cache(cache_key, response_population.json())
    
    return response_population.json()