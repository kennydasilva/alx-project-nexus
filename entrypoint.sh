#!/bin/sh
# entrypoint.sh

set -e

echo "=== entrypoint: starting ==="
echo "DEBUG: SECRET_KEY set? -> $( [ -n "$SECRET_KEY" ] && echo yes || echo no )"
echo "DEBUG: DATABASE_URL set? -> $( [ -n "$DATABASE_URL" ] && echo yes || echo no )"

trap 'echo "entrypoint: failed with exit $?: see above"' ERR

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput || echo "collectstatic exited non-zero"

echo "Starting Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
