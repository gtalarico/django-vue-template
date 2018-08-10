# Collect Static is Done Manually
# because Heroku runs `collectstatic`` before `yarn build`
# so dist is not ready
python manage.py collectstatic --noinput
python manage.py migrate
