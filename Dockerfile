FROM python:3.10.13-slim-buster
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
CMD python app.py