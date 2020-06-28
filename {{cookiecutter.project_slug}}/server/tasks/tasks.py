from celery import Celery
from functools import lru_cache
import joblib
import random

def make_prediction(X):
    model = joblib.load('model.joblib')
    return model.predict(X).tolist()

app = Celery(
    'tasks', 
    broker="redis://redis", 
    backend="redis://redis"
    # broker="pyamqp://"
)

@app.task(name='tasks.tasks.add')
def add(x: int, y: int) -> int:
    return random.randint(10, 100)

@app.task(name='tasks.tasks.predict_iris')
def predict_iris(X):
    try:
        return make_prediction(X)
    except BaseException:
        return "Error"