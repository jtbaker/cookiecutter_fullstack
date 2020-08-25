FROM tiangolo/uvicorn-gunicorn-fastapi

WORKDIR /app/src


COPY ./requirements.txt /app/src/requirements.txt

RUN ["pip3", "install", "--upgrade", "pip"]
RUN ["pip3", "install", "-r", "requirements.txt"]



# CMD ["gunicorn", "main:app",  "-w",  "4",  "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]