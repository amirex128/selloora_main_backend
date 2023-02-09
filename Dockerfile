FROM python:3.11-alpine AS builder
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN apk update
RUN apk add gcc
RUN apk add musl-dev
RUN apk add build-base
RUN apk add python3-dev
RUN apk add mariadb-dev
RUN apk add mysql-client
RUN apk add libstdc++
RUN apk add openssl-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
RUN python3 manage.py collectstatic --noinput --clear
RUN python3 manage.py makemigrations
ENTRYPOINT ["python3"]
CMD ["/usr/local/bin/gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi"]
