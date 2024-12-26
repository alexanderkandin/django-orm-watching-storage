import os
from environs import Env


env = Env()
env.read_env()

# Получение значений переменных
key = env.str('KEY')
PASSWORD_DB = env.str('PASSWORD_DB')
LOGIN_DB = env.str('LOGIN_DB')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': LOGIN_DB,
        'PASSWORD': PASSWORD_DB,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv("KEY")

DEBUG = env.bool('DJANGO_DEBUG', default=False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


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
