from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def root():
    return {"data": "Example-8 is regaring Query Parameter Models"}
