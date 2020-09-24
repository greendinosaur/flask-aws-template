FROM python:3.7.7-slim-buster

COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY my_app.py config.py log_config.yaml boot.sh ./
RUN chmod +x ./boot.sh

ENV FLASK_APP my_app.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]

