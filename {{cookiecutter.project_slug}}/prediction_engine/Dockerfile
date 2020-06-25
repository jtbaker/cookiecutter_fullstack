FROM continuumio/miniconda3

WORKDIR /home

COPY ./requirements.txt /home/requirements.txt

RUN ["pip", "install", "-r", "requirements.txt"]

CMD ["python", "placeholder.py"]