FROM python:3.11-alpine AS builder
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN apk update
RUN apk add meson
RUN apk add sudo
RUN apk add gcc
RUN apk add build-base
RUN apk add musl-dev
RUN apk add python3-tkinter
RUN apk add tiff-dev
RUN apk add jpeg-dev
RUN apk add openjpeg-dev
RUN apk add zlib-dev
RUN apk add freetype-dev
RUN apk add lcms2-dev
RUN apk add libwebp-dev
RUN apk add tcl-dev
RUN apk add tk-dev
RUN apk add harfbuzz-dev
RUN apk add fribidi-dev
RUN apk add libimagequant-dev
RUN apk add libxcb-dev
RUN apk add libpng-dev
RUN apk add openssl
RUN apk add openssl-dev
RUN apk add libstdc++
RUN apk add mysql-client
RUN apk add mariadb-dev
RUN apk add python3-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
RUN python3 manage.py collectstatic --noinput --clear
RUN python3 manage.py makemigrations
ENTRYPOINT ["python3"]
CMD ["/usr/local/bin/gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi"]
