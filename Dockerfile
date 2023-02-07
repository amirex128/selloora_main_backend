FROM python:3.11-alpine AS builder
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN apk update
RUN apk add --virtual build-deps gcc python3-dev musl-dev build-base mariadb-dev
RUN apk add --no-cache mariadb-dev
RUN apk add mysql-client
RUN apk del build-deps
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