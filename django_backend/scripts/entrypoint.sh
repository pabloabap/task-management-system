#!/bin/bash
set -euo pipefail

echo "Migrate..."
python manage.py migrate
echo "Runserver..."
python manage.py shell < /app/scripts/default_db_values.py
exec python manage.py runserver ${DJANGO_HOST}:${DJANGO_PORT}