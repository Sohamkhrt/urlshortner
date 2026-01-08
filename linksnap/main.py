from fastapi import FastAPI
from .schemas import URLInput

app = FastAPI()

@app.get("/")
def root():
    return {"message": "root working, app online"}

@app.post("/url")
def create_url(data:URLInput):
    return {"received":data.recieved_url}