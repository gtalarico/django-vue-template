# Collect Static is Done Manually
# because Heroku runs `collectstatic`` before `yarn build`
# so dist is not ready
echo "Collecting Static..."
python manage.py collectstatic --noinput
echo "Migrate..."
python manage.py migrate
