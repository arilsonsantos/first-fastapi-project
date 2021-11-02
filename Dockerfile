FROM ubuntu:latest

WORKDIR /app

RUN apt update && apt upgrade -y

RUN apt install -y -q python3-pip python3-dev
RUN apt install -y -q build-essential python3-pip python3-dev

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY app/ /app

ENV ACCESS_LOG=${ACCESS_LOG:-/proc/1/fd/1}
ENV ERROR_LOG=${ERROR_LOG:-/proc/1/fd/2}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
