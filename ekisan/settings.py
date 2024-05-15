"""
Django settings for ekisan project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from pathlib import Path
import os
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bv@*m=fn+=4enh9brpji-7dh*thv#8g4eq506hve(ji_pox=i6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ekisan-3.onrender.com','localhost']


# Application definition

INSTALLED_APPS = [
    'accounts.apps.AccountsConfig',
    'farmer.apps.FarmerConfig',
    'dealer.apps.DealerConfig',
    'seller.apps.SellerConfig',
    'deliveryman.apps.DeliverymanConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'farmer.middleware.middleware.AuthMiddleware1',
    #'dealer.middleware.middleware.AuthMiddleware2',

]

ROOT_URLCONF = 'ekisan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates' )],
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

WSGI_APPLICATION = 'ekisan.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'ekisan',
#         'USER': 'postgres',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#     }
# }

DATABASES = {
    'default': dj_database_url.parse('postgres://ekisan_user:r5wHoTRi7BVgVCwloJi1nITHxMDHdBbg@dpg-cp1vbui1hbls7397v5rg-a.oregon-postgres.render.com/ekisan')
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

STATIC_URL = '/static/'  # Changed from 'static/' to '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Set STATIC_ROOT for deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# Configure STATICFILES_STORAGE for production
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)
    
ASGI_APPLICATION = 'ekisan.routing.application'

RAZORPAY_KEY_ID= 'rzp_test_ZJnfFgi9V8tgCE'
RAZORPAY_KEY_SECRET= 'ItM5DIKdXHVXXUrNusMXTOvN'

GOOGLE_MAPS_API_KEY ='AIzaSyA4ok42pz99BZiplrtRQHs4kzCVQH_fxfQ'
KEY='2GYalXMe31736j6Cz6lRiRHC5N1Yc4zn',
URL='https://www.mapquestapi.com/geocoding/v1/address?key='


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # SMTP server host
EMAIL_PORT = 587  # SMTP server port (usually 587 for TLS/STARTTLS)
EMAIL_USE_TLS = True  # Whether to use TLS/STARTTLS for secure connection
EMAIL_HOST_USER = 'talhahamid.syed@gmail.com'  # Your Gmail email address
EMAIL_HOST_PASSWORD = 'talhahamid9229'  # Your Gmail password