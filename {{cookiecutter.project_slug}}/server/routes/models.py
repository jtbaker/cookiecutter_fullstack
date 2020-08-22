# from prediction.predictions import WorkerSettings
import pandas as pd
from arq import connections
from arq.connections import ArqRedis, create_pool, RedisSettings
from fastapi import APIRouter, Depends
import logging

# import tasks
# from tasks import tasks
# from arq import create_pool
import arq
import random
import asyncio
from pydantic import BaseModel
from typing import List, Union
from datetime import datetime
# from pyarrow import serialize, deserialize
from pyarrow import serialize, deserialize
from enum import Enum
# class IrisInput(BaseModel):
#     x: List[List[int]]


class AllowedModels(str, Enum):
    reg = "testmodel"



router = APIRouter()

task_queue: arq.connections.ArqRedis

@router.on_event("startup")
async def startup():
    global task_queue
    task_queue = await arq.create_pool(
        RedisSettings(host="redis"),
        job_serializer = lambda x: serialize(x).to_buffer().to_pybytes(),
        job_deserializer = deserialize
    )


# def predictor():
#     return tasks.predict_iris.delay


# @router.get("/model/fakedata")
# async def fake_data():
#     num_1: int = random.randint(1, 10)
#     num_2: int = random.randint(2, 400)
#     response = tasks.add.delay(num_1, num_2) # type: ignore
#     counter = 0
#     start = datetime.now()
#     while not response.ready():
#         await asyncio.sleep(5)
#         end = datetime.now()
#         counter += 1
#         print(f"Counter: counter")
#     print(f"Total time: {end - start}")
#     return response.get()

# @router.post("/model/iris")
# async def iris(X: List[List[int]], handler = Depends(predictor)):
#     response = handler(X) # type: ignore
#     while not response.ready():
#         await asyncio.sleep(0.05)
#     return response.get(timeout=5)


class FakeData(BaseModel):
    a: Union[int, float]
    b: Union[int, float]
    c: Union[int, float]


@router.post("/model/testmodel")
async def predict_model(X: List[FakeData]) -> List[Union[int, float]]:
    df = pd.DataFrame.from_records([v.dict() for v in X])
    job = await task_queue.enqueue_job("predict", "testmodel", df)
    result = await job.result(timeout=5000)
    return result


# class WorkerSettings:
#     redis_settings = RedisSettings(host="cookiecutter-redis")
#     job_serializer = lambda x: serialize(x).to_buffer().to_pybytes()
#     job_deserializer = deserialize