FROM python:3.11-alpine AS builder
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN apk update
RUN apk add gcc
RUN apk add musl-dev
RUN apk add build-base
RUN apk add build-deps
RUN apk add --no-cache --update mariadb-dev python3-dev
RUN apk add mysql-client
RUN apk add libstdc++
RUN apk add openssl-dev
RUN apk add mariadb-connector-c-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
RUN addgroup -S docker
RUN adduser -S --shell /bin/bash --ingroup docker vscode
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]