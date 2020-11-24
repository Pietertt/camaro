FROM tensorflow/tensorflow

WORKDIR /model

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

COPY . .

#RUN pip install -r requirements.txt