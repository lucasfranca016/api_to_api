import requests

def get_city_info(country: str):
    cities_url = "https://countriesnow.space/api/v0.1/countries/cities"
    capital_url = "https://countriesnow.space/api/v0.1/countries/capital"
    
    response_cities = requests.post(cities_url, json={
        "country": country
    })
    
    response_capital = requests.post(capital_url, json={
        "country": country
    })
    
    info_cities = response_cities.json()
    
    info_capital = response_capital.json()
    
    cities = info_cities["data"] # Seleciona as cidades no JSON
    
    capital = info_capital["data"]["capital"] # Seleciona a capital no JSON
    
    return {
        "error": info_cities["error"],
        "msg": info_cities["msg"],
        "data": {
            "total_cities" : len(cities),
            "capital" : capital,
            "cities" : cities
    }}