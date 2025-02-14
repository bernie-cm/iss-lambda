FROM public.ecr.aws/lambda/python:3.9

RUN pip install pandas sqlalchemy requests

WORKDIR /app
COPY main.py main.py

ENTRYPOINT ["python3", "main.py"]
