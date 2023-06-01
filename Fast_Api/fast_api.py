from datetime import datetime
from typing import Text, Optional
from uuid import uuid4 as uuid

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
posts = []


# Post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False


@app.get("/")
def index():
    return {"mensaje": "Bienvenidos a mi Api"}


@app.get("/read")
def get_posts():
    return posts


@app.post("/posts")
def save_post(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]


@app.get('/read/{title}')
def get_post_title(title: str):
    for post in posts:
        if post["title"] == title:
            return post
    raise HTTPException(status_code=404, detail="Titulo no encontrado")


@app.delete("/delete/{title}")
def delete_post_title(title: str):
    for index, post in enumerate(posts):
        if post['title'] == title:
            posts.pop(index)
            return {f"message": f"El post se ha eliminado correctamente : {title}"}
    raise HTTPException(status_code=404, detail="Titulo no encontrado")


@app.put("/update/{title}")
def update_post(title: str, updatedPost: Post):
    for index, post in enumerate(posts):
        if post["title"] == title:
            posts[index]["title"] = updatedPost.title
            posts[index]["author"] = updatedPost.author
            posts[index]["content"] = updatedPost.content
            return {"message": "El Post se ha actualizado"}
    raise HTTPException(status_code=404, detail="Titulo no encontrado")


@app.get("/posts/{post_id}")
def get_post_by_id(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post no encontrado")
