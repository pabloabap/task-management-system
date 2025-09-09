import os
import django
from apps.tasks.models import Tag, Task

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get("DEFAULT_SUPERUSER_USER", "admin")
email = os.environ.get("DEFAULT_SUPERUSER_EMAIL", "admin@example.com")
password = os.environ.get("DEFAULT_SUPERUSER_PSWD")

if not password:
    raise SystemExit("DEFAULT_SUPERUSER_PSWD not set")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created:", username)
else:
    print("Superuser already exists:", username)

default_tags = ["IT", "FI", "SA"]

for tag in default_tags:
    Tag.objects.get_or_create(name=tag)



