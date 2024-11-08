from typing import Annotated, Union, List

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"data": "example11 is about the Body-Nested Models"}

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results