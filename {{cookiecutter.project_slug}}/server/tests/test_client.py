import pytest
from typing import Union, Any
from fastapi.testclient import TestClient

import pandas as pd

# from server.main import app
# from main import app

# from ..main import app
from main import app, get_cache
from db.models import User, Base


# class Cache:
#     def get(self, key: str) -> Any:
#         return getattr(self, key)

#     def set(self, key: str, value: Any):
#         setattr(self, key, value)

#     def delete(self, key):
#         delattr(self, key)
    

# def override_get_cache():
#     return Cache


# app.dependency_overrides[get_cache] = override_get_cache

# def test_name():



def test_user():
    with TestClient(app) as test_client:
        params = {'name': "Jason"}
        response = test_client.get("/name", params=params).json()
        print(response)
        assert response == params, "Params not equal"
        # response = test_client.get("/").json()
        print(response)
    # assert response.get("name") == "Jason"


def test_iris():
    with TestClient(app) as test_client:
        df = pd.read_csv('./tests/data/iris.csv')
        arr = df.values.tolist()
        response = test_client.post("/model/iris", json=arr).json()
        print("Response is", response)
        # print(response)
        assert len(response) == len(arr)
