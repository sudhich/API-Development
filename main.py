from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel



app = FastAPI()

class Post(BaseModel):
    title: str
    content: str




@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/post")
def root():
    return {"message": "Hello how are you"}

"""@app.post("/createposts")
def create_post(payload: dict=Body()):
    print(payload)
    return {"title_by_user": payload['title'],"content_by_user":payload['content']}"""

@app.post("/createposts")
def create_post(new_post:Post):
    print(new_post)
    print(new_post.title)
    return {"data":"new_post"}