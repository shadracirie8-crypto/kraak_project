import os
from pathlib import Path

from decouple import config
import dj_database_url


# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent


# Security

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    '.onrender.com',
    '127.0.0.1',
    'localhost',
]


CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
]


# Application definition

INSTALLED_APPS = [

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # Applications locales
    'core',
    'services',
    'programs',
    'contact',
    'accounts',
]


MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    # Static files Render
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


ROOT_URLCONF = 'kraak_project.urls'


TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]


WSGI_APPLICATION = 'kraak_project.wsgi.application'



# Database PostgreSQL Render

DATABASES = {

    'default': dj_database_url.config(

        default=config('DATABASE_URL'),

        conn_max_age=600

    )

}



# Password validation

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },


    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },


    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },


    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]



# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files

STATIC_URL = '/static/'


STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'static')

]


STATIC_ROOT = BASE_DIR / 'staticfiles'


STATICFILES_STORAGE = (

    'whitenoise.storage.CompressedManifestStaticFilesStorage'

)



# Media files (images, uploads)

MEDIA_URL = '/media/'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Authentication

LOGIN_REDIRECT_URL = 'redirect_after_login'

LOGOUT_REDIRECT_URL = 'home'

LOGIN_URL = 'login'


AUTH_USER_MODEL = 'accounts.User'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Security production

SECURE_SSL_REDIRECT = False


SESSION_COOKIE_SECURE = True


CSRF_COOKIE_SECURE = True


SECURE_HSTS_SECONDS = 31536000


SECURE_HSTS_INCLUDE_SUBDOMAINS = True


SECURE_HSTS_PRELOAD = True