FROM python:3.6-stretch

RUN apt-get update
RUN apt-get install -y libpq-dev zip

COPY app/ /narrative
RUN pip install -r /narrative/requirements.txt

VOLUME /narrative
WORKDIR /narrative