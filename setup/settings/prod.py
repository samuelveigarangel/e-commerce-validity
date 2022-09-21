import django_on_heroku
import dj_database_url
from dotenv import load_dotenv, find_dotenv

from .base import *

SECRET_KEY = config("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [
    "e-commerce-validity.herokuapp.com",
]

DEBUG_PROPAGATE_EXPECTIONS = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "MYAPP": {
            "handlers": ["console"],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

# Heroku Settings

load_dotenv(find_dotenv())

DATABASES = {
    "default": dj_database_url.config(default="sqlite://db.slite3")
}


django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES["default"]["OPTIONS"]["sslmode"]
