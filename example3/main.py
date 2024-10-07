from fastapi import FastAPI

app = FastAPI()

Comments = { 
    1: "very good",
    2: "not good",
    3: "excellent"
}

@app.get("/")
def index():
    return {"Data": "blog list"}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get("/blog/{id}")
def abc(id: int):
    return {"Data": id}

@app.get("/blog_comments/{blog_id}/")
def comments(blog_id: int):
    return {'data': {'comments': Comments[blog_id]}}
