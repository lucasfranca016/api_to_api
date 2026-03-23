from fastapi import FastAPI


app = FastAPI()


@app.get("/city")
def city_function():
    return {"temporary return"}

@app.get("/country")
def country_function():
    return {"temporary return"}