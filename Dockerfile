FROM python:3.12-alpine 

RUN mkdir -p/usr/src/app/app

WORKDIR /usr/src/app

COPY requirements.txt main.py ./
COPY app ./app

RUN pip install -r requirements.txt

CMD ls -l