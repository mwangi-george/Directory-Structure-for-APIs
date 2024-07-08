FROM python:3.12-alpine 

RUN mkdir -p /usr/src/app/app

WORKDIR /usr/src/app

COPY requirements.txt main.py ./
COPY user_app ./user_app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app"]
