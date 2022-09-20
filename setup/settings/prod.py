import django_on_heroku
from decouple import config

from setup.settings.dev import ALLOWED_HOSTS

from .base import *

SECRET_KEY = config("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [
    "e-commerce-validity.herokuapp.com",
]
