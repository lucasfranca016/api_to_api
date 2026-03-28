from fastapi import FastAPI
from pydantic import BaseModel
from custom_libs.country_functions import get_country_info
from custom_libs.city_functions import get_city_info

class Country(BaseModel):
    country_name: str


app = FastAPI()

@app.get("/{country}/cities")
def city_function(country: str):
    
    cities_info = get_city_info(country=country)

    return cities_info
    
    
@app.post("/country")
def country_function(country: Country):

    country_info = get_country_info(country.country_name)

    return country_info
