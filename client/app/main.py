from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return requests.get('https://nginx/api/hello', verify=False).text
