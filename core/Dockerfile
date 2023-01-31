FROM python:latest
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN mkdir -p /usr/src/app/data

FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install cron
COPY cron /etc/cron.d/sample
RUN cron
CMD service cron start && tail -f