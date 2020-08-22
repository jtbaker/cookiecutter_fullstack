FROM python:3.8-slim

WORKDIR /home

RUN ["pip", "install", "sklearn", "joblib", "pandas", "numpy", "pyarrow", "arq"]

CMD ["arq", "worker.WorkerSettings"]