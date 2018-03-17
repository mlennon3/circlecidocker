FROM python:3.6-slim-stretch

RUN apt-get update && apt-get install -y wget

ADD . /home

WORKDIR /home

RUN pip install -r requirements.txt

CMD ["python", "/home/circdock/manage.py", "test"]

