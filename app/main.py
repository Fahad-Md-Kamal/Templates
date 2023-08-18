from fastapi import FastAPI
from app.cache_setup import redis_cache

from app.routes import auth_routes, post_routes, user_routes

app = FastAPI()

@app.on_event("startup")
async def startup():
    redis_cache()


app.include_router(post_routes.router)
app.include_router(user_routes.router)
app.include_router(auth_routes.router)
