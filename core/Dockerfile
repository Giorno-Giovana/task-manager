FROM ubuntu:latest
RUN mkdir -p /task-manager/
WORKDIR /task-manager/
COPY script.sh /task-manager/
RUN apt-get update && apt-get -y install cron
COPY cron /etc/cron.d/test
RUN crontab /etc/cron.d/test
CMD cron && tail -f


