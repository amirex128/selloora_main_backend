FROM python:3.11-alpine AS builder
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN apk update
RUN apk meson sudo gcc build-base musl-dev add py3-setuptools python3-tkinter tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev libxcb-dev libpng-dev openssl openssl-dev libstdc++ mysql-client mariadb-dev python3-dev



RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
RUN python3 manage.py collectstatic --noinput --clear
RUN python3 manage.py makemigrations
ENTRYPOINT ["python3"]
CMD ["/usr/local/bin/gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi"]
