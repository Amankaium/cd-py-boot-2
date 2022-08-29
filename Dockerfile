FROM python:3.10-alpine
WORKDIR /lamp/
COPY requirements.txt /lamp/
RUN pip install -r requirements.txt
COPY . /lamp/
