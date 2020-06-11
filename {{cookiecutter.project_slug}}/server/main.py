from fastapi import FastAPI
from views import views

# i/o
import databases
import aioredis

redis = None

# database = databases.Database("postgresql://{")

app = FastAPI()

app.include_router(views.router, prefix="/home")

@app.on_event('startup')
async def startup():
    global redis
    redis = await aioredis.create_redis_pool(
        'redis://redis'
    )
    # await database.connect()

@app.get("/")
async def index(name: str = None):
    if name is None:
        name = await redis.get("name", encoding="utf-8")
    else:
        redis.set('name', name)
    return f"Hello, {name}"
