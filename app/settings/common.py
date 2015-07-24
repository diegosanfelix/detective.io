# -*- coding: utf-8 -*-
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from os.path import dirname
import os
# for relative paths
root = lambda x: os.path.join(os.path.abspath( dirname(dirname(__file__))), x)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TASTYPIE_FULL_DEBUG = DEBUG

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Custom data directory
DATA_ROOT = root('data')

ADMINS = (
    ('Pierre Romera', 'hello@pirhoo.com'),
)

DEFAULT_FROM_EMAIL = 'Detective.io <contact@detective.io>'
SERVER_EMAIL       = DEFAULT_FROM_EMAIL

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db'
    }
}

NEO4J_DATABASES = {
    'default' : {
        'HOST': "127.0.0.1",
        'PORT': 7474,
        'ENDPOINT':'/db/data'
    }
}

DATABASE_ROUTERS        = ['neo4django.utils.Neo4djangoIntegrationRouter']
SESSION_ENGINE          = "django.contrib.sessions.backends.db"
AUTHENTICATION_BACKENDS = ('app.detective.auth.CaseInsensitiveModelBackend',)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

DATETIME_FORMATS = [
    '%Y-%m-%dT%H:%M:%S.%fZ', # '2006-10-25T14:30:59.000Z'
    '%Y-%m-%d %H:%M:%S.%fZ', # '2006-10-25T14:30:59.000Z'
    '%Y-%m-%dT%H:%M:%S.%f',  # '2006-10-25T14:30:59.000'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000'
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d'               # '2006-10-25'
]

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = root('media')

UPLOAD_ROOT = os.path.join(MEDIA_ROOT, 'upload')

THUMBNAIL_SIZES = {
    'mini' : (60, 40),
    'small' : (60, 60),
    'medium' : (300, 200)
}

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/public/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = root('staticfiles')

LOGIN_URL = "/admin"
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    ('custom_d3',  root('static/custom_d3') ),
    root("detective/bundle/client/"),
    root("detective/bundle/.build/"),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv('SECRET_KEY', '#_o0^tt=lv1k8k-h=n%^=e&amp;vnvcxpnl=6+%&amp;+%(2!qiu!vtd9%')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
CACHE_BYPASS_URLS               = (
    r"/api/(?P<user>[\w\-\.]+)/(?P<topic>[\w\-]+)/v1/summary/graph/",
    r"/api/(?P<user>[\w\-\.]+)/(?P<topic>[\w\-]+)/v1/summary/export/",
    r"/api/(?P<user>[\w\-\.]+)/(?P<topic>[\w\-]+)/v1/summary/forms/"
)

MIDDLEWARE_CLASSES = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'app.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'app.middleware.crossdomainxhr.XsSharing',
    # add urlmiddleware after all other middleware.
    'urlmiddleware.URLMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

SUIT_CONFIG = {
    'ADMIN_NAME': 'Detective.io',
    'MENU_EXCLUDE': ('registration', 'tastypie'),
}

ROOT_URLCONF = 'app.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'app.wsgi.application'

TEMPLATE_DIRS = (
    root('detective/templates'),
    root('detective/bundle/client/app'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Remove BeautifulSoup requirement
COMPRESS_PARSER = 'compressor.parser.HtmlParser'
COMPRESS_ENABLED = False
#INTERNAL_IPS = ('127.0.0.1',)

TASTYPIE_DEFAULT_FORMATS = ['json', 'jsonp']


INSTALLED_APPS = (
    # 'suit' must be added before 'django.contrib.admin'
    'suit',
    'neo4django.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    # Allow CORS
    'corsheaders',
    # Thumbnails generator
    'easy_thumbnails',
    # Sign up activation
    'registration',
    # Compresses linked and inline JavaScript or CSS into a single cached file.
    'compressor',
    # API generator
    'tastypie',
    # Email backend
    'password_reset',
    # Manage migrations
    'south',
    # Rich text editor
    'tinymce',
    # Redis queue backend
    "django_rq",
    # Internal
    'app.detective',
    'app.detective.topics.common',
    'app.detective.topics.energy',
    'app.detective.permissions',
)

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Two-weeks activation window
ACCOUNT_ACTIVATION_DAYS = 14
# Send or not an activation email
ACCOUNT_ACTIVATION_ENABLED = True

# MemCachier configuration took from https://devcenter.heroku.com/articles/memcachier#django
def get_cache():
  # We do this complicated cache defenition so that on a local machine (where
  # MEMCACHIER_SERVERS won't be defined), the try fails and so we use the
  # inbuilt local memory cache of django.
  try:
    os.environ['MEMCACHE_SERVERS']  = os.environ['MEMCACHIER_SERVERS'].replace(',', ';')
    os.environ['MEMCACHE_USERNAME'] = os.environ['MEMCACHIER_USERNAME']
    os.environ['MEMCACHE_PASSWORD'] = os.environ['MEMCACHIER_PASSWORD']
    return {
        'default': {
            'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
            'TIMEOUT': 500,
            'BINARY': True,
            'OPTIONS': {
                'tcp_nodelay': True,
            }
        }
    }
  except:
    # Use django local development cache (for local development).
    return {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
            #'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': '/tmp/django_cache',
        }
    }

CACHES = get_cache()

# Redis Queues
# RQ_SHOW_ADMIN_LINK will override the default admin template so it may interfere
# with other apps that modifies the default admin template.
RQ_SHOW_ADMIN_LINK = True
RQ_CONFIG = {
    'URL'  : os.getenv('REDISTOGO_URL', None) or os.getenv('REDISCLOUD_URL', None) or 'redis://localhost:6379',
    'DB'   : 0,
    'ASYNC': True
}
RQ_QUEUES = {
    'default': RQ_CONFIG,
    'high'   : RQ_CONFIG,
    'low'    : RQ_CONFIG
}

APP_TITLE = 'Detective.io'

# GROUPS of user / Plans
# NOTE: keys limited to 10 characters
PLANS = [
    {"free"       : {"max_investigation" :  3, "max_entities"  :  100 }},
    {"jane"       : {"max_investigation" :  5, "max_entities"  :  500 }},
    {"hank"       : {"max_investigation" : -1, "max_entities"  :  1000}},
    {"sherlock"   : {"max_investigation" : -1, "max_entities"  : -1   }},
    {"enterprise" : {"max_investigation" : -1, "max_entities"  : -1   }}
]
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'django.utils.log.NullHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
        'app.detective': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'rq.worker': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}
