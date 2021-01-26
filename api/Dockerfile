FROM tensorflow/tensorflow:nightly-jupyter

WORKDIR /api

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

#RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY . .

EXPOSE 5000

CMD ["flask", "run"]