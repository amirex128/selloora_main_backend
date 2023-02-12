FROM python:3.11-alpine AS builder
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN apk update
RUN apk sudo
RUN apk gcc
RUN apk build-base
RUN apk musl-dev
RUN apk python3-tkinter
RUN apk tiff-dev
RUN apk jpeg-dev
RUN apk openjpeg-dev
RUN apk zlib-dev
RUN apk freetype-dev
RUN apk lcms2-dev
RUN apk libwebp-dev
RUN apk tcl-dev
RUN apk tk-dev
RUN apk harfbuzz-dev
RUN apk fribidi-dev
RUN apk libimagequant-dev
RUN apk libxcb-dev
RUN apk libpng-dev
RUN apk openssl
RUN apk openssl-dev
RUN apk libstdc++
RUN apk mysql-client
RUN apk mariadb-dev
RUN apk python3-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
RUN python3 manage.py collectstatic --noinput --clear
RUN python3 manage.py makemigrations
ENTRYPOINT ["python3"]
CMD ["/usr/local/bin/gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi"]
