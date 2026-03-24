from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/{country}/cities")
def city_function(country: str):
    cities_url = "https://countriesnow.space/api/v0.1/countries/cities"

    response_cities = requests.post(cities_url, json={
        "country": country
    })
    return response_cities.json()


@app.get("/country")
def country_function():
    return {"temporary return"}