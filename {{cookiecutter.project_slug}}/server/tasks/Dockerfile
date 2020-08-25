FROM continuumio/miniconda3

WORKDIR /home

COPY ./requirements.txt /home/requirements.txt

RUN ["pip", "install", "-r", "requirements.txt"]

# CMD ["python", "tasks.py"]
CMD ["celery", "-A", "tasks", "worker", "-l", "info"]