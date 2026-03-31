import requests

city_cache = {}

def get_city_info(country: str):  
    country = country.lower()
    
    if country not in city_cache:
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
        
        try:
            cities = info_cities["data"] # Seleciona as cidades no JSON
        
            capital = info_capital["data"]["capital"] # Seleciona a capital no JSON
            
            city_data = {
                "error": info_cities["error"],
                "msg": info_cities["msg"],
                "data": {
                    "total_cities" : len(cities),
                    "capital" : capital,
                    "cities" : cities
            }}
            
            city_cache[country] = city_data
            
        except KeyError:
            print('O país não foi encontrado')
        
            city_data = {
                "error": True,
                "msg": "country not found",
            }
        
        return city_data
        
    else:
        return city_cache[country]