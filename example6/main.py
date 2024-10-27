
from fastapi import FastAPI, Query
from typing import Annotated
from enum import Enum

app = FastAPI()

@app.get("/")
async def root():
    return {"data": "Example6 is about extra validation on optional parameter"}

#Optional parameter for validation using Query functionality that is importanted from fastapi
@app.get("/items/")
async def read_items(q: Annotated[str| None, Query(max_length=50)] ):
    result = {"items": [{"item_id": "Foo"}, {"item_id":"Bar"}] }
    if q :
        result.update({"q": q})
    return result
    

#when q is query parameter is used multiple time in the URL path 
@app.get("/books/")
async def read_books(q : Annotated[list | None, Query()] = ["foo", "app"]):
    query_items = {"q" : q}
    return query_items

#adding the title and description in the query
@app.get("/toys/")
async def read_toys(
    q: Annotated[str | None, Query(title="Query string", 
                                   description = "Query string for the items to search in the database that have a good match",
                                   min_length=3)] = None,
):
    results = {"toys": [{"toy_id": "Foo"}, {"toy_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#using alias method
@app.get("/birds/")
async def details_birds(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#who to state the depricated 