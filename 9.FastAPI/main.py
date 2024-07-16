from fastapi import FastAPI 
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float 
    is_offer: bool = None

@app.get("/")
def display_index():
    return "Hello World"

@app.get("/welcome")
def welcome_msg():
    return "Welcome to class"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def save_item(item_id:int, item: Item):
    return {"Item_name": item.name,
            "Item_price": item.price,
            "Item_id":item_id }