FROM python:3.6-slim-stretch AS base

RUN apt-get update && apt-get install -y wget

ADD . /home

WORKDIR /home

RUN pip install -r requirements.txt

FROM python:3.6-slim-stretch

COPY --from=base /usr/local/lib/python3.6/site-packages/ /usr/local/lib/python3.6/site-packages/

WORKDIR /home/circdock

ENTRYPOINT ["./entry.sh"]

