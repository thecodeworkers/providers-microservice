FROM python:3.8-alpine
RUN mkdir /micro
WORKDIR /micro
COPY ./requirements.txt /micro/
RUN apk add g++ linux-headers
RUN pip install -r requirements.txt
