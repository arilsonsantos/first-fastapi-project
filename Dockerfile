FROM python:3.9-slim

WORKDIR /app

RUN apt update && apt upgrade -y

RUN pip3 install --upgrade pip

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY app/ /app

ENV ACCESS_LOG=${ACCESS_LOG:-/proc/1/fd/1}
ENV ERROR_LOG=${ERROR_LOG:-/proc/1/fd/2}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
