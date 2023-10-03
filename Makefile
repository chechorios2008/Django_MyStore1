

runserver:
	py manage.py runserver --settings=settings.local

makemigrations:
	py manage.py makemigrations --settings=settings.local

migrate:
	py manage.py migrate --settings=settings.local