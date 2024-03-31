from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return requests.get('http://nginx/server/api/hello').text
