FROM python:3.12-alpine

RUN pip install pipenv

RUN mkdir -p/usr/src/app

WORKDIR /the/workdir/path