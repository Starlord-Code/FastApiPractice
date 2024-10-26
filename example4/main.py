from enum import Enum

from fastapi import FastAPI

app = FastAPI()

class ModelName(str, Enum):
    harsha = "Harsha D"
    basanth = "Basanth N"
    vikram = "Vikram V"


@app.get("/")
async def root():
    return {"Data":"This example-4 for Enum"}

@app.get("/users/{user_name}")
async def display(user_name: ModelName):
    if user_name is ModelName.harsha:
        return {"user_name": ModelName.harsha , "details": "He is from Rajahmundry"}
    elif user_name.value ==  ModelName.basanth:
        return {"user_name": ModelName.basanth  , "details": "He is from West Godavari"}
    elif user_name == ModelName.vikram:
        return {"user_name": ModelName.vikram , "details": "He is from Mars"}
    
    return {"user_name": "Not present" , "details": "user details not present"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_location": file_path}