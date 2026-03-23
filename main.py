from fastapi import FastAPI
from pydantic import BaseModel
from custom_libs.country_functions import get_country_info

app = FastAPI()

class Country(BaseModel):
    country_name: str

@app.get("/city")
def city_function():
    return {"temporary return"}

@app.post("/country")
def country_function(country: Country):

    country_info = get_country_info(country.country_name)

    return country_info