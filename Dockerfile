FROM python:latest
ENV PYTHONUNBUFFERED 1

RUN mkdir /robot-docker
WORKDIR /robot-docker
ADD . /robot-docker/

RUN pip install -r requirements.txt