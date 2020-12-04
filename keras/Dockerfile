FROM python:3.6-stretch
COPY . /app

WORKDIR /app

#RUN pip install -r requirements.txt

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1