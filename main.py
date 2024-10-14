from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app= FastAPI()

@app.get("/")
async def root():
    return{"message":"Hello World !"}

@app.get("/posts")
async def we_are_getting_post():
    return{"text":"happy day"}

class Post(BaseModel):
    title: str
    content: str

@app.post("/createposts")

async def create_post(newpost:Post):
    print (newpost)
    return{"data":"newpost"}

