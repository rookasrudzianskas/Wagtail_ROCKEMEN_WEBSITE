from .base import *
import os

DEBUG = False
SECRET_KEY = 'jyt7_upl188kp71f-19^)7+57s_t-#m!bd%%d#=3)k89r(eba%'
ALLOWED_HOSTS = ['localhost', 'rocketman.learnwagtail.com', '*']

cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": 'rocketman',
        "USER": 'rocketman',
        "PASSWORD": 'xfHjB^F2p9s*zhqFT6cNx2s',
        "HOST": 'localhost',
        "PORT": "",
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://2a96bb5715ab426594b4d231f3fa39a4@o573055.ingest.sentry.io/5723160",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass
