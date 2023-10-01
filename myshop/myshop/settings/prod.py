import os
from .base import *
import dj_database_url


DEBUG = False

ADMINS = [
    ('anasantos', 'adm.anasantosjesus@gmail.com'),
]

ALLOWED_HOSTS = ['boutiquedaana.com', 'www.boutiquedaana.com.br']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '741147123',
        'HOST': 'localhost',  # or the IP where your DB is hosted
        'PORT': '5442',  # leave as an empty string to use the default port
    }
}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)



# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
# prod.py
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
