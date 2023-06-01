from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid

app = FastAPI()


class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False


class Blog:
    def __init__(self):
        self.posts = []

    def get_posts(self):
        return self.posts

    def create_post(self, post: Post):
        post.id = str(uuid())
        self.posts.append(post)
        return post

    def update_post(self, post_id: str, post: Post):
        for i in range(len(self.posts)):
            if self.posts[i].id == post_id:
                self.posts[i] = post
                return self.posts[i]
        return None

    def delete_post(self, post_id: str):
        for i in range(len(self.posts)):
            if self.posts[i].id == post_id:
                return self.posts.pop(i)
        return None


blog = Blog()


@app.get("/")
def index():
    return {"mensaje": "¡Hola, mundo desde fast aPi!"}


@app.get("/posts")
def get_posts():
    return blog.get_posts()


@app.post("/posts")
def create_post(post: Post):
    return blog.create_post(post)


@app.put("/posts/{post_id}")
def update_post(post_id: str, post: Post):
    return blog.update_post(post_id, post)


@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    return blog.delete_post(post_id)
