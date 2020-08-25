FROM python:3.8-slim

WORKDIR /home
COPY requirements.txt /home/requirements.txt

RUN ["apt-get" , "update"]
RUN ["apt-get", "install", "libgomp1"]
RUN ["pip", "install", "-r", "requirements.txt"]

CMD ["arq", "worker.WorkerSettings"]