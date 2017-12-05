from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cataloglibrary',              # Or path to database file if using sqlite3.
        'USER': 'root',      # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'CONN_MAX_AGE': 0     # No persistend connections
    }
}

import cloudinary

cloudinary.config(
    cloud_name="gajemeeuit",
    api_key="756932446195744",
    # api_secret="https://cloudinary.com/console"
)