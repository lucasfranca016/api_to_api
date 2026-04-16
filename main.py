from fastapi import FastAPI
from pydantic import BaseModel
from custom_libs.country_functions import get_country_info
from custom_libs.city_functions import get_city_info
from tenacity import RetryError

class Country(BaseModel):
    country_name: str


app = FastAPI()

@app.get("/{country}/cities")
def city_function(country: str):
    try:
        cities_info = get_city_info(country=country)
         
    except RetryError:
        print('After a few attempts, it was not possible to connect')
        cities_info = {
                "error": True,
                "msg": "failed to connect"
            }
 
    return cities_info
    
@app.post("/country")
def country_function(country: Country):
    try:
        country_info = get_country_info(country.country_name)
    
    except RetryError:
        print('After a few attempts, it was not possible to connect')
        
        country_info = {
            "error": True,
            "msg": "failed to connect"
        }
    
    return country_info