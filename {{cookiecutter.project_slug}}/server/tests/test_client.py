import pytest
from typing import Union, Any
from fastapi.testclient import TestClient

import pandas as pd

# from server.main import app
# from main import app

# from ..main import app

from server.src.main import app
from server.src.db.models import get_db, Base
# from src.db.models import User, Base

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

# engine = create_engine("postgresql://postgres:postgres@pg:5432/postgres")


engine = create_engine("sqlite:///", connect_args = {"check_same_thread": False})

Base.metadata.create_all(bind=engine)

TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


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

test_client = TestClient(app)

def test_user():
    params = {'name': "Jason"}
    response = test_client.get("/name", params=params).json()
    print(response)
    assert response == params, "Params not equal"
    # response = test_client.get("/").json()
    # assert response.get("name") == "Jason"


# def test_iris():
#     with TestClient(app) as test_client:
#         df = pd.read_csv('./tests/data/iris.csv')
#         arr = df.values.tolist()
#         response = test_client.post("/model/iris", json=arr).json()
#         print("Response is", response)
#         # print(response)
#         assert len(response) == len(arr)
