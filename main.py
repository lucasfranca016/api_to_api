from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/{country}/cities")
def city_function(country: str):
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
    
    cities = info_cities["data"] # Seleciona as cidades
    
    capital = info_capital["data"]["capital"] # Seleciona a capital
    
    return {
        "error": info_cities["error"],
        "msg": info_cities["msg"],
        "data": {
            "total_cities" : len(cities),
            "capital" : capital,
            "cities" : cities
    }}

@app.get("/country")
def country_function():
    return {"temporary return"}