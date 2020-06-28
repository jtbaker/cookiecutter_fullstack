from fastapi import FastAPI
from views import views
from routes import token, actions, models
# from prediction_engine import add
from security.authentication import authenticate_user
from serialization.serializers import User

# i/o
import databases
import aioredis

# redis = None

# database = databases.Database("postgresql://{user}:{password}@{host}:5432/{dbname}")

app = FastAPI()

# app.include_router(views.router, prefix="/")
app.include_router(token.router)
app.include_router(actions.router)
app.include_router(models.router)
# @app.on_event("startup")
# async def startup():
    # global redis
    # redis = await aioredis.create_redis_pool("redis://redis")
    # await database.connect()


async def login(name: str, password: str):
    user = await authenticate_user(username=name, password=password)
    # user.aw


@app.get("/")
async def index(name: str = None):
    if name is None:
        name = await redis.get("name", encoding="utf-8")
        # redis.
    else:
        redis.set("name", name)
    return f"Hello, {name}\n\n"
