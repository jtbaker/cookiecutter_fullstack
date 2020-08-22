from prediction.predictions import WorkerSettings
from arq import create_pool
from arq.connections import RedisSettings




class WorkerSettings:
    functions = []