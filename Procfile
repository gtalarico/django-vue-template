change_db: python manage.py makemigrations api
release: python manage.py migrate
web: gunicorn backend.wsgi --log-file -
