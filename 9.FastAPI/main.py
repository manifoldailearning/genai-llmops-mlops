from fastapi import FastAPI 
from typing import Union

app = FastAPI()

@app.get("/")
def display_index():
    return "Hello World"

@app.get("/welcome")
def welcome_msg():
    return "Welcome to class"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}