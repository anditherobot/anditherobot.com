FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y swig libssl-dev dpkg-dev netcat

RUN mkdir /django-docker
WORKDIR /django-docker
ADD requirements.txt /django-docker/
RUN pip install -U pip
ADD requirements.txt /code/
RUN pip install -Ur /code/requirements.txt
ADD . /django-docker/