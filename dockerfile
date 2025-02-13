FROM python:3.13.2

RUN pip install pandas sqlalchemy requests psycopg2

WORKDIR /app
COPY main.py main.py

ENTRYPOINT ["python3", "main.py"]