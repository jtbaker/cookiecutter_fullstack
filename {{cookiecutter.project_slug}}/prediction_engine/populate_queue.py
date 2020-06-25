import redis as r
import numpy as np
import pandas as pd
import pyarrow as pa
from string import ascii_uppercase
redis = r.Redis("redis")

def generate_array():
    return np.random.rand(5000, 4) * 4

def random_df():
    arr = generate_array()
    return pd.DataFrame(generate_array(), columns=[ascii_uppercase[i] for i in range(arr.shape[1])])


# def r

def populate_queue():
    dfs = [random_df() for n in range(20)]
    for df in dfs:
        write_df(df)

def encode_dataframe(df: pd.DataFrame):
    return pa.serialize_pandas(df).to_pybytes()

def decode_dataframe(bytes):
    return pa.deserialize_pandas(bytes)

def write_df(df):
    serialized = encode_dataframe(df)
    redis.rpush('task_queue', serialized)