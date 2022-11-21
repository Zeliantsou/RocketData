import os
from distutils.util import strtobool

from dotenv import load_dotenv
from pathlib import Path


load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = bool(strtobool(os.environ.get('DEBUG')))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(', ')

API_PREFIX = 'api/v1/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_filters',

    'company',
    'product',
    'reference',
    'user',
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

ROOT_URLCONF = 'src.urls'

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

WSGI_APPLICATION = 'src.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DATABASE_NAME'),
        'USER': os.environ.get('DJANGO_DATABASE_USER'),
        'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD'),
        'HOST': os.environ.get('DJANGO_DATABASE_HOST'),
        'PORT': os.environ.get('DJANGO_DATABASE_PORT'),
    }
}

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

RABBITMQ_DEFAULT_USER = os.environ.get('RABBITMQ_DEFAULT_USER')
RABBITMQ_DEFAULT_PASS = os.environ.get('RABBITMQ_DEFAULT_PASS')
RABBITMQ_PORT_FIRST = os.environ.get('RABBITMQ_PORT_FIRST').split(':')[0]
RABBITMQ_PORT_SECOND = os.environ.get('RABBITMQ_PORT_SECOND').split(':')[0]
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')

CELERY_BROKER_URL = 'amqp://' + RABBITMQ_DEFAULT_USER + ':' + RABBITMQ_DEFAULT_PASS + \
                    '@' + RABBITMQ_HOST + ':' + RABBITMQ_PORT_FIRST + '/%2F'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'rpc://' + RABBITMQ_DEFAULT_USER + ':' + RABBITMQ_DEFAULT_PASS + \
                    '@' + RABBITMQ_HOST + ':' + RABBITMQ_PORT_SECOND + '/%2F'
CELERY_ACCEPT_CONTENT = ('application/json',)
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

SOURCE_EMAIL = os.environ.get('SOURCE_EMAIL')

# AWS_ACCESS_KEY_ID = os.environ.get('RABBITMQ_HOST')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_DEFAULT_REGION = os.environ.get('AWS_DEFAULT_REGION')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# ALLOWED_FILE_EXTENSIONS = ('jpeg', 'jpg', )

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
