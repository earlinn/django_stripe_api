import os

from .base import BASE_DIR

DEBUG = False
ALLOWED_HOSTS = [
    "web",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost/*",
]
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": os.getenv("DB_NAME", default="postgres"),
        "USER": os.getenv("POSTGRES_USER", default="postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="postgres"),
        "HOST": os.getenv("DB_HOST", default="db"),
        "PORT": os.getenv("DB_PORT", default="5432"),
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, "static")
