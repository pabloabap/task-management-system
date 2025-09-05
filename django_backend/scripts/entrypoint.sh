#!/bin/bash
set -euo pipefail

env
echo "Migrate..."
python manage.py migrate
echo "Runserver..."
exec python manage.py runserver ${DJANGO_HOST}:${DJANGO_PORT}
# Si se quiere crear un super usuario por defecto:
# python manage.py createsuperuser