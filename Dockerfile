FROM python:3.8-slim-buster

COPY api2.py /app/app.py
WORKDIR /app

RUN pip install flask

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]
