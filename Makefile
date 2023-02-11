m:
	python manage.py migrate

mm:
	python manage.py makemigrations

cs:
	python manage.py collectstatic --noinput --clear

su:
	python manage.py createsuperuser

rs:
	python manage.py runserver

