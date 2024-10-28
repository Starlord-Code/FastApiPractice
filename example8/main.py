from typing import Annotated, Literal
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

class FilterParams(BaseModel):
    #this avoid the extra query parameter if they send it
    model_config = {"extra": "forbid"}
    
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get("/")
async def root():
    return {"data": "Example-8 is regaring Query Parameter Models"}

@app.get("/items")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

