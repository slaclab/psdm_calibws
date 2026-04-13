FROM python:3.14.3-alpine

ENV TZ="America/Los_Angeles"
ENV LANG=en_US.UTF-8

RUN apk add bash

COPY src/requirements.txt /

RUN pip3 install -r requirements.txt

RUN mkdir /work

COPY src /work/psdmcalibws

WORKDIR /work/psdmcalibws


