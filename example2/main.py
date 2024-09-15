from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel 
import sys
from redis_om.model.model import ExpressionProxy

app = FastAPI()

class ExpressionProxyWrapper(ExpressionProxy):
    @classmethod
    def __get_pydantic_core_schema__(cls, handler):
        return handler.generate_schema(cls)

redis = get_redis_connection(
    host = "redis-11015.c321.us-east-1-2.ec2.redns.redis-cloud.com",
    port = 11015,
    password = "ZZqWhgxwJDmnQCiECyyi0L4pgbdr345y",
    decode_responses = True 
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)
# The commented out code block defines a Python class named `Product` that inherits from `HashModel`.
# The `Product` class has attributes `name` (string), `price` (float), and `quantity` (integer). The
# `Meta` class inside `Product` specifies the database connection to be used, which in this case is a
# Redis database connection named `redis`.

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta: 
        database= redis

    class Config:
        arbitrary_types_allowed = True  

    

#get the product details from the redis database from RedisJSON

@app.get("/get-products")
def all():
    return Product.all_pks() 

@app.post("/create-product")
def create_product(product: Product):
    return product.save()

# get te python version details which python version is the uvicorn is running

@app.get("/python-version")
async def get_python_version():
    return {"python_version": sys.version}