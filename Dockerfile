FROM python:3.10-slim-buster

WORKDIR /istro-back

COPY /requirements/requirements.txt /istro-back/requirements/

RUN pip install --upgrade pip

RUN apt-get update && apt-get upgrade -y

RUN pip install -r requirements/requirements.txt

COPY . /istro-back


EXPOSE 8000 9000