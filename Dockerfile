FROM python:alpine
RUN mkdir -p /task-manager/
RUN mkdir -p /task-manager/core
RUN mkdir -p /task-manager/adapters
RUN mkdir -p /task-manager/data
ENV PYTHONPATH "${PYTHONPATH}:/task-manager/"
WORKDIR /task-manager/
COPY /adapters/adapter.py /task-manager/adapters/adapter.py
COPY /core/main.py /task-manager/core/main.py
COPY /data/test /task-manager/data/test
COPY cron cron
RUN crontab cron
CMD crond -f
