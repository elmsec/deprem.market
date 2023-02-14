FROM python:3.9.6-alpine

WORKDIR /usr/src/depremmarket

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./wait-for.sh .
COPY ./requirements.txt .
COPY ./requirements.dev.txt .

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
        libressl-dev libffi-dev cargo \
    && apk add postgresql-dev \
    && pip install --upgrade pip \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install -r requirements.dev.txt \
    && apk del build-deps

RUN apk add curl

ENTRYPOINT ["/usr/src/depremmarket/scripts/entrypoint.sh"]
