

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*ska8)d8fix4dcqlza*avam88ts$usa20s@=&+stv(cu22*!^1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

"""
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME':'TPFINAL',
        'Trusted_Connection':'yes',
        'HOST': 'localhost',
        'OPTIONS':{
        	'driver':'SQL Server Native Client 11.0',
        }
    },
}
"""

