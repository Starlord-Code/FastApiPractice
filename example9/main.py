
from typing import Annotated, Literal

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
class User(BaseModel):
    username: str
    full_name: str | None = None
    

@app.get("/")
async def root():
    return {"data": "example9 is about Body Multiple Parameters"}

@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results
    
#mutliple body parameter 
@app.put("/material/{material_id}")
async def update_item(
    material_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {"material_id": material_id, "item": item, "user": user, "importance": importance}
    return results

#Embed a single Body parameter
# item : Item = Body(embed=True)

@app.put("/packages/{package_id}")
async def update_package(
    package_id: int,
    item: Annotated[Item, Body(embed=True)]
):
    result = {"package_id": package_id, "item": item}
    return result 