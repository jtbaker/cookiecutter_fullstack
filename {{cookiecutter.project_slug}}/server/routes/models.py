from fastapi import APIRouter, Depends
# import tasks
from tasks import tasks
import random
import asyncio
from pydantic import BaseModel
from typing import List

# class IrisInput(BaseModel):
#     x: List[List[int]]


router = APIRouter()


def predictor():
    return tasks.predict_iris.delay


@router.get("/model/fakedata")
async def fake_data():
    num_1: int = random.randint(1, 10)
    num_2: int = random.randint(2, 400)
    response = tasks.add.delay(num_1, num_2) # type: ignore
    while not response.ready():
        await asyncio.sleep(0.05)
    return response.get(timeout=5)

@router.post("/model/iris")
async def iris(X: List[List[int]], handler = Depends(predictor)):
    response = handler(X) # type: ignore
    while not response.ready():
        await asyncio.sleep(0.05)
    return response.get(timeout=5)