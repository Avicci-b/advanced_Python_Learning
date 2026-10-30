from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

items = []

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.get("/items")
def list_items():
    return {"items": items}

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item created", "item": item}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]