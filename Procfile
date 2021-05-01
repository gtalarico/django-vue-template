change_db: python manage.py makemigrations api
release: python manage.py migrate
cron: python manage.py corntab run
web: gunicorn backend.wsgi --log-file -
