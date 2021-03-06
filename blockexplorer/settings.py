"""
Django settings for blockexplorer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from psycopg2cffi import compat
compat.register()

import re
import dj_database_url
import raven

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_PATH = BASE_DIR
LOCALE_PATHS = (PROJECT_PATH + "/locale/",)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('DEBUG') == 'True':
    DEBUG = True
else:
    DEBUG = False
if os.getenv('TEMPLATE_DEBUG') == 'True':
    TEMPLATE_DEBUG = True
else:
    TEMPLATE_DEBUG = False

# DDT can cause extreme slowness clocking template rendering CPU times
if os.getenv('DISABLE_DEBUG_TOOLBAR') == 'False':
    DISABLE_DEBUG_TOOLBAR = False
else:
    DISABLE_DEBUG_TOOLBAR = True

ALLOWED_HOSTS = [
        '127.0.0.1',
        'www.0xify.com',
        'localhost'
        ]

ADMINS = (
    ('AndrewBC', 'dawn.gurl@gmail.com'),
)

IGNORABLE_404_URLS = (
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'annoying',
    'raven.contrib.django.raven_compat',
    'crispy_forms',
    'storages',
    'apps.addresses',
    'apps.transactions',
    'apps.users',
    'apps.emails',
    'apps.services',
)

MIDDLEWARE_CLASSES = (
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blockexplorer.urls'

WSGI_APPLICATION = 'blockexplorer.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Parse database configuration from $DATABASE_URL
# http://stackoverflow.com/a/11100175
DB = {
    'driver': os.environ.get("DB_DRIVER", None),
    'user': os.environ.get("DB_USER", None),
    'pass': os.environ.get("DB_PASS", None),
    'host': os.environ.get("DB_HOST", None),
    'port': os.environ.get("DB_PORT", None),
    'name': os.environ.get("DB_NAME", None),
}
if not DB['user'] and not DB['pass'] and not DB['host'] and not DB['port']:
    print("SQLite Mode")
    DJ_DEFAULT_URL = os.getenv('DJ_DEFAULT_URL', u"%s://%s" % (DB['driver'], DB['name']))
else:
    print("PostgreSQL Mode")
    DJ_DEFAULT_URL = os.getenv('DJ_DEFAULT_URL', u"%s://%s:%s@%s:%s/%s" % (DB['driver'], DB['user'], DB['pass'], DB['host'], DB['port'], DB['name']))

DATABASES = {'default': dj_database_url.config(default=DJ_DEFAULT_URL)}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.AuthUser'
LOGIN_URL = '/blocks/login'

# Languages
LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('en-us', 'English'),
)
if os.getenv('ENABLE_TRANSLATIONS') == 'False':
    ENABLE_TRANSLATIONS = False
else:
    ENABLE_TRANSLATIONS = True
    MIDDLEWARE_CLASSES += ('django.middleware.locale.LocaleMiddleware',)
    LANGUAGES += (('es', 'Spanish'),)

# Yay crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_ALLOWED_TEMPLATE_PACKS = ('bootstrap', 'bootstrap3')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/blocks/static/'

TEMPLATES = [
 {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(PROJECT_PATH, 'templates'),],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
 },
]


PRODUCTION_DOMAIN = 'www.0xify.com'
STAGING_DOMAIN = 'TODO'
SITE_DOMAIN = os.getenv('SITE_DOMAIN', PRODUCTION_DOMAIN)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False

# SSL and BASE_URL settings for Production, Staging and Local:
if SITE_DOMAIN in (PRODUCTION_DOMAIN, STAGING_DOMAIN):
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    BASE_URL = 'https://%s/blocks/' % SITE_DOMAIN
    # FIXME:
    # SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    MIDDLEWARE_CLASSES += ('blockexplorer.middleware.SSLMiddleware',)
else:
    BASE_URL = 'http://%s/blocks/' % SITE_DOMAIN
    if not DISABLE_DEBUG_TOOLBAR:
        # FIXME: this should work on staging too, but I can't get it to work with gunicorn
        DEBUG_TOOLBAR_PATCH_SETTINGS = True


IS_PRODUCTION = (SITE_DOMAIN == PRODUCTION_DOMAIN)

if IS_PRODUCTION:
    EMAIL_DEV_PREFIX = False
else:
    EMAIL_DEV_PREFIX = True
    if not DISABLE_DEBUG_TOOLBAR:
        # Enable debug toolbar on local and staging
        MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE_CLASSES
        INSTALLED_APPS += ('debug_toolbar', )

if not DISABLE_DEBUG_TOOLBAR:
    # Debug Toolbar
    INTERNAL_IPS = (
            '127.0.0.1',
            'localhost',
            )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'blockexplorer.context_processors.get_user_units',
)

BLOCKCYPHER_API_KEY = os.getenv('BLOCKCYPHER_API_KEY')
BLOCKCYPHER_PUBLIC_KEY = '35efab90903cbaf2551efe4134798e'

POSTMARK_SMTP_SERVER = 'smtp.postmarkapp.com'
POSTMARK_SENDER = 'AndrewBC <AndrewBC@0xify.com>'
POSTMARK_TEST_MODE = os.getenv('POSTMARK_TEST_MODE', False)
POSTMARK_API_KEY = os.getenv('POSTMARK_API_KEY')
if not POSTMARK_API_KEY:
    print('WARNING: without a POSTMARK_API_KEY you cannot send emails')

WEBHOOK_SECRET_KEY = os.getenv('WEBHOOK_SECRET_KEY')
if not WEBHOOK_SECRET_KEY:
    print('WARNING: without a WEBHOOK_SECRET_KEY you cannot receive webhooks')

EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'

SENTRY_DSN = os.getenv('SENTRY_DSN')

# Wallet Name
WNS_URL_BASE = 'https://pubapi.netki.com/api/wallet_lookup'

DEFAULT_USER_UNIT = 'btc'

RAVEN_CONFIG = {
    'dsn': os.getenv('RAVEN_DSN'),
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}

# http://scanova.io/blog/engineering/2014/05/21/error-logging-in-javascript-and-python-using-sentry/
LOGGING = {
    'version': 1,
    # https://docs.djangoproject.com/en/dev/topics/logging/#configuring-logging
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

if DEBUG:
    print('-'*75)
    print('SITE_DOMAIN is set to %s' % SITE_DOMAIN)
    print("If you're using webhooks locally, be sure this is correct")
    print('-'*75)
