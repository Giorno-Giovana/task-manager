FROM python
RUN apt-get update && apt-get -y install cron
ENV TZ=Europe/Moscow
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /task-manager/
COPY . .
RUN crontab cron
CMD cron -f log
