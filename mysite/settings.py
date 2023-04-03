"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
import django_heroku
import dj_database_url
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-edw@tm^z%nonby^jfjs)awkz9$&^9uw221ljne$d_9(07i66^7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = ('cart')



# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mathfilters',
    'fontawesomefree',
   



    'account',
    'shop',
    'checkout',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#         'OPTIONS': {
#             'timeout': 30,  # increase timeout to 30 seconds
#         },
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dc5q416hccfd7h',
        'USER': 'tdlkkpcnddolva',
        'PASSWORD': 'fcd29d45fa5eb5ad7beb95be13f45a225c62f31a020d3a62254cb6b16c2f9483',
        'HOST': 'ec2-3-93-160-246.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'



STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

django_heroku.settings(locals())


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STRIPE_SECRET_KEY = 'sk_test_51M5ok1HEEvdlG8h96eeSWlAAiRgPMgyK70HdS7ykJCARy8VCbSmzV7JmmNC5hNKIZzslAvXhEOX5Nu88nmBU1bb500EKVRhGRp'
STRIPE_PUBLISHABLE_KEY = 'pk_test_51M5ok1HEEvdlG8h9CGAFVUHDHjBOddf2bRJpHzg22L15K9njT5bQKMhy5HjUQlrVVRvF4spm0QgnPEDAo1H7iZCC007m42OPom'
STRIPE_ENDPOINT_SECRET = 'whsec_689b09e63a8c1366e40c9a99a74ea515650a4cf13a6ad6657356415909a37e30'


JAZZMIN_SETTINGS = {
    'site_title': "Dajngo Ecommerce ",
    
    "site_header": "Dajngo Ecommerce ",
    
    
    "site_brand": "Dajngo Ecommerce ",
    
    
    "site_logo": None,
    
    
    "welcome_sign": "Welcome Your Dashbord",
    
    
     "copyright": "Django Ecommerce.ltd",
}