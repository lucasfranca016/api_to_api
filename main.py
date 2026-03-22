from fastapi import FastAPI
import requests


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/teste")
def read_root():
    resposta = requests.get("https://countriesnow.space/api/v0.1/countries/states")
    return resposta.text