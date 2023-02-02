FROM ubuntu:latest
RUN apt-get update && apt-get -y install cron
COPY cron /etc/cron.d
RUN cron
CMD service cron start && tail -f

FROM python:latest
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/
#RUN mkdir -p /usr/src/app/data
#CMD python3 main.py