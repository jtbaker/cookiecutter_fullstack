import arq
from arq.connections import RedisSettings
from enum import Enum
from typing import Any, Union
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
import numpy as np
from pyarrow import serialize, deserialize
import joblib
import pyarrow
import asyncio

ModelRegressor = Union[
    LinearRegression, DecisionTreeRegressor, RandomForestRegressor, SVR
]


class ModelKeys(str, Enum):
    testmodel = "testmodel"


class AllowedModels(str, Enum):
    reg = "testmodel"


models = {"testmodel": joblib.load("./tests/model.joblib")}


async def predict(ctx, model_key: ModelKeys, X: Any) -> np.array:
    model: ModelRegressor = models[model_key]
    return model.predict(X).round(3).tolist()


async def main():
    redis = await arq.create_pool(
        RedisSettings(host="redis"), 
        job_serializer = lambda x: serialize(x).to_buffer().to_pybytes(),
        job_deserializer = deserialize
    )


class WorkerSettings:
    redis_settings = RedisSettings(host="redis")
    functions = [predict]
    
    job_serializer = lambda x: serialize(x).to_buffer().to_pybytes()
    job_deserializer = deserialize


async def main():
    redis = await arq.create_pool(RedisSettings(host="cookiecutter-redis"))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())