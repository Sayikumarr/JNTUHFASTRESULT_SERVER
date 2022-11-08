web: gunicorn jntuhresults.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
heroku config:set DISABLE_COLLECTSTATIC=1
manage.py migrate