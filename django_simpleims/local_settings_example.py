"""
Local settings for this instance - prod.
"""
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gM!3p#&&1vytP!lQm67gM!3p#&&1vytP!lQm67sOnL%#%icmJVWsOnL%#%icmJVW'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 15768000

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['FQDN']

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

####
# Instance settings
####

INSTANCE_FQDN = 'https://example.com'
INSTANCE_LABEL_TEXT = 'IMS ID'
# In mm
INSTANCE_LABEL_WIDTH = 38
INSTANCE_LABEL_HEIGHT = 19
