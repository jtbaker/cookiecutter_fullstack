FROM tiangolo/uvicorn-gunicorn-fastapi

COPY ./requirements.txt /app/requirements.txt

RUN ["pip3", "install", "--upgrade", "pip"]
RUN ["pip3", "install", "-r", "requirements.txt"]

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]