import os
from .base import *


DEBUG = False

ADMINS = [
    ('cesar', 'adm.anasantosjesus.com'),
]

ALLOWED_HOSTS = ['boutiquedaana.com', 'www.boutiquedaana.com.br']



# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
# prod.py
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
