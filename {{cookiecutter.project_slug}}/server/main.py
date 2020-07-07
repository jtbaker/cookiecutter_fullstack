from fastapi import FastAPI, Depends
# from .views import views
# from views import views
# from .routes import token, actions, models
# from prediction_engine import add
# from .security import authenticate_user
# from .serialization import User
# from . import views
# , security, serialization, routes, tasks
# import .views, .security, .serialization, .routes, .tasks

# from .routes import token, actions, models
# from server.routes import token, actions, models
# import .views
# import .views
# from . import routes 
# import routes
# from routes import token, actions, models

from routes import token, actions, models
from dotenv import load_dotenv
from os import getenv

load_dotenv()

SECRET_KEY = getenv('SECRET_KEY', default = 'NO KEY - DANGER')

# import routes
# import token, actions, models
# import .security
# import .serialization

# from security import authenticate_user

# i/o
import databases
import aioredis


# database = databases.Database("postgresql://{user}:{password}@{host}:5432/{dbname}")

app = FastAPI()

redis = None

def get_cache():
    return redis

# app.include_router(views.router, prefix="/")
app.include_router(token.router)
app.include_router(actions.router)
app.include_router(models.router)
@app.on_event("startup")
async def startup():
    global redis
    redis = await aioredis.create_redis_pool("redis://cookiecutter-redis")
    # await database.connect()


# async def login(name: str, password: str):
#     user = await security.authenticate_user(username=name, password=password)
#     # user.aw


@app.get("/")
async def index(name: str = None, cache = Depends(get_cache)):
    if name is None:
        name = await cache.get("name", encoding="utf-8")
        # redis.
    else:
        await cache.set("name", name)
    return f"""Hello, {name}
    """


@app.get("/name")
async def get_name(name: str, cache = Depends(get_cache)):
    # redis.set("name", name)
    return {"name": name}