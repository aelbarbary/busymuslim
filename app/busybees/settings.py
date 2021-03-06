"""
Django settings for busybees project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from boto3.session import Session

ADMINS =(('admin','busymuslimbees@gmail.com'),)
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
SERVER_EMAIL = 'xyz@gmail.com'
EMAIL_HOST_USER = os.environ['BUSYBEES_EMAIL_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['BUSYBEES_EMAIL_PASSWORD']
EMAIL_PORT = 587
SEND_BROKEN_LINK_EMAILS = True
CORS_ORIGIN_ALLOW_ALL = True

# AUTH_USER_MODEL = 'busybeesapp.Profile'
ACCOUNT_ACTIVATION_DAYS=7
boto3_session = Session(aws_access_key_id=os.environ['ACCESS_KEY'],
                        aws_secret_access_key=os.environ['SECRET_KEY'],
                        region_name='us-west-2')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': u"%(asctime)s [%(levelname)-8s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'aws': {
            # you can add specific format for aws here
            'format': u"%(asctime)s [%(levelname)-8s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': []
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("BASE_DIR:" + BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kva1tbcca-76u$4@dd#1)!f3tr%a1j3n)e6^8a5exa()+2oo0r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ '*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'busybeesapp',
    'dashboard',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'busybees.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
                'busybeesapp.context_processors.google_analytics',

            ],
        },
    },
]

WSGI_APPLICATION = 'busybees.wsgi.application'

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'busybees',
         'HOST': os.environ['BUSYBEES_DB_HOST'],
         'USER': os.environ['BUSYBEES_DB_USER'],
         'PASSWORD': os.environ['BUSYBEES_DB_PASSWORD']
     }
 }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AWS_STORAGE_BUCKET_NAME = 'busybees'
AWS_S3_HOST = "s3-us-west-2.amazonaws.com"
AWS_ACCESS_KEY_ID = os.environ['BUSYBEES_S3_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['BUSYBEES_S3_SECRET_KEY']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# STATIC_ROOT = os.path.join(BASE_DIR, "/static")
STATIC_URL = '/static/'

MEDIA_ROOT = '/www/busybees/media'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
     os.path.join(BASE_DIR, "static"),
     '/var/www/static/',
 ]

# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, 'media')
#
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
    }

REGISTRATION_OPEN = True                # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'  # The page users are directed to if they are not logged in,
# SECURE_SSL_REDIRECT=True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

GOOGLE_ANALYTICS_PROPERTY_ID = os.environ['GA_TRACKING_ID']
GOOGLE_ANALYTICS_DOMAIN = 'tamkeen.us:8001'
