from .base import *

DEBUG = False
ALLOWED_HOSTS = [
    host.strip()
    for host in env.list('ALLOWED_HOSTS', default=[])
    if host.strip()
]

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
