from fastapi import FastAPI
from custom_libs import city_functions

app = FastAPI()

@app.get("/{country}/cities")
def city_function(country: str):
    return city_functions.get_city_info(country=country)

@app.get("/country")
def country_function():
    return {"temporary return"}