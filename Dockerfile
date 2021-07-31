FROM python:3.8-alpine

RUN apk add build-base

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt