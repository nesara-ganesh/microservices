FROM python:3.8-alpine

MAINTAINER Manipal School of Information Sciences

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --update \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*
  
RUN python3 -m pip install requests 

COPY ./app /app

CMD python app.py
