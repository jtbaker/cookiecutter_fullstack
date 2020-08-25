# from prediction.predictions import WorkerSettings
import pytest
from arq import create_pool
import joblib
from arq.connections import RedisSettings
from worker.worker import predict
import pandas as pd

@pytest.mark.asyncio
async def test_model():
    df = pd.DataFrame({
        "a": [1, 2, 3, 4, 5],
        "b": [40, 50, 80, 200, 100],
        "c": [20, 100, 5, 40, 80]
    })

    predictions = await predict(None, 'testmodel', X=df)


    assert len(df) == len(predictions), "Predictions were different length than model."
    assert predictions['prediction'].min() > 0, "Minimum prediction less than zero"
