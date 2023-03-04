FROM python
RUN apt-get update && apt-get -y install cron
WORKDIR /task-manager/
COPY . .
RUN crontab cron
CMD cron -f log
