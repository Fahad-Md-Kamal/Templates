from fastapi import FastAPI

from app.routes import post_routes, user_routes, auth_routes

app = FastAPI()


app.include_router(post_routes.router)
app.include_router(user_routes.router)
app.include_router(auth_routes.router)
