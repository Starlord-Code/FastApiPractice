
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum



app = FastAPI()

class Material(str, Enum):
    Iron = "ie"
    Magnesium = "mg" 

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
async def root():
    return {"data": "Example-5 is for Request Body"}

# @app.post("/items/")
# async def create_item(item: Item, material_type: Material ):
#     return item, material_type.value

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict