FROM python:3.10-alpine
WORKDIR /lamp/
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt /lamp/
RUN pip install -r requirements.txt
COPY . /lamp/
