from fastapi import FastAPI

from app.routes import posts

app = FastAPI()


app.include_router(posts.router, prefix="/posts", tags=["POSTS"])
# app.include_router(comments.router, prefix="/comments", tags=["comments"])
