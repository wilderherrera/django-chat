"""
Django settings for chatRealTime project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)o6ynk9)rdvt+r10=v6$_(&!4k$fhwf=zyratx%is#2v%4j@!q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGGING = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message} {asctime}",
            "style": "{",
        },
    },
    "filters": {"require_debug_true": {
        "()": "django.utils.log.RequireDebugTrue",
    },
    },
    "disable_existing_loggers": False,
    "handlers": {
        "console_critical": {
            "level": "CRITICAL",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "console_warning": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        }, "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "debug.log",
            "filters": ["require_debug_true"],
            "formatter": "verbose",
        }
    },
    "root": {
        "handlers": ["console_warning", "file", "console_critical"],
        "level": "WARNING",
    },
}

# Application definition
LOGOUT_REDIRECT_URL = "/v1/home"

LOGIN_REDIRECT_URL = "/v1/home"

LOGIN_URL = "/auth/v1/login"

STATIC_ROOT = os.path.join(BASE_DIR, 'tailwind_app/static/')
COMPRESS_ROOT = os.path.join(BASE_DIR, 'tailwind_app/static/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'tailwind_app/static'),
    os.path.join(BASE_DIR, 'django_browser_reload/static'),

)

COMPRESS_ENABLED = True

STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'compressor',
    'chat',
    "daphne",
    'channels',
    'django.contrib.staticfiles',
    'authentication',
    'tailwind',
    'tailwind_app',
    'django_browser_reload'

]
TAILWIND_APP_NAME = 'tailwind_app'

INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",

]

ROOT_URLCONF = 'chatRealTime.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'chatRealTime/templates')],
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

WSGI_APPLICATION = 'chatRealTime.wsgi.application'
ASGI_APPLICATION = 'chatRealTime.asgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "chatdjango",
        "USER": "postgres",
        "PASSWORD": "root",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
