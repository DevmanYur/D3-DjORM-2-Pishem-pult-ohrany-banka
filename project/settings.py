import os
from environs import Env


env = Env()
env.read_env()


DATABASES = {
    'default': {
        'ENGINE': env("DB_ENGINE"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool("DEBUG_FALSE", "DEBUG_TRUE")

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = [env("ALLOWED_HOSTS")]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
