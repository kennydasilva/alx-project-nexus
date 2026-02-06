#!/bin/sh
# entrypoint.sh

# Aplica migrates e collectstatic
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Inicia gunicorn
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
