from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

Comments = { 
    1: "very good",
    2: "not good",
    3: "excellent"
}

#for the request body we have imported the pydantic
class Blog(BaseModel):
    title: str
    body: Optional[str] = None
    published: bool

@app.get("/")
def index(limit: int, published: bool, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    elif sort:
        return {"Data": f"{limit} blogs with sort {sort} from the database"}
    else:
        return {"Data": f"{limit} blogs from the database"} 


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get("/blog/{id}")
def abc(id: int):
    return {"Data": id}

@app.get("/blog/{blog_id}/comments")
def comments(blog_id: int, limit = 10):
    return {'data': {'comments': Comments[blog_id]}}

@app.post("/blog")
def create_blog(item: Blog):
    return {"data": f"blog is created with title :  {item.title}"}

#for debugging with breakpoints in VS code
if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0', port=8000)