# from prediction.predictions import WorkerSettings
from arq import create_pool
import joblib
from arq.connections import RedisSettings
from ..worker import predict
import pandas as pd


def test_model():

    model = joblib.load('../model.joblib')
    df = pd.DataFrame({
        "a": [1, 2, 3, 4, 5],
        "b": [40, 50, 80, 200, 100],
        "c": [20, 100, 5, 40, 80]
    })


    predictions = model.predict(df).prediction


    assert len(df) == len(predictions), "Predictions were different length than model."
    assert predictions.min() > 0, "Minimum prediction less than zero"
