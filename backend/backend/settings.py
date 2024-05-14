from pathlib import Path
import os
from os import environ
from datetime import timedelta



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = environ.get('SECRET_KEY','&k(rj62%vplbnlv9leim8=8=#4)g#vvv$r=4wwoht1_#^wj3^a')
SECRET_KEY = environ.get('SECRET_KEY','wd-0&nml&ien6#8*!8ptm11u76bo#o0a1gsqk^xdp$27925$=c')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(environ.get('DEBUG', default = 1))


ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', '*').split(' ')


if "CSRF_TRUSTED_ORIGINS" in environ:
    CSRF_TRUSTED_ORIGINS = environ.get('CSRF_TRUSTED_ORIGINS').split(' ')


# RMQ_HOST = environ.get('RMQ_HOST', '127.0.0.1')
# RMQ_PORT = environ.get('RMQ_PORT', 5672)
# RMQ_USER = environ.get('RMQ_USER', 'admin')
# RMQ_PASS = environ.get('RMQ_PASS', 'admin')

# Application definition

INSTALLED_APPS = [
    'model_utils',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_filters',
    'drf_spectacular',
    'rest_framework',
    'corsheaders', 
    'apps.user',
    'apps.taskpage',
    'apps.kpp',
    # 'apps.kpp.apps.MyAppConfig',
    ]

SPECTACULAR_SETTINGS = {
    'TITLE': 'Django5 Test Swagger API',
    'DESCRIPTION': 'Django5 Test Swagger API description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True
    # OTHER SETTINGS
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# CORS_ALLOW_METHODS = (
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# )

# CORS_ALLOW_HEADERS = (
#     "accept",
#     "authorization",
#     "content-type",
#     "user-agent",
#     "x-csrftoken",
#     "x-requested-with",
# )

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3001",
# ]

# CSRF_TRUSTED_ORIGINS = [
#     "http://localhost:3001",
# ]
# CORS_ALLOW_ALL_ORIGINS: True
# CORS_ALLOW_PRIVATE_NETWORK: True

ROOT_URLCONF = 'backend.urls'

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
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': environ.get('POSTGRES_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': environ.get('POSTGRES_DB', 'helpdesk'),
        'USER': environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD', 123),
        'HOST': environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': environ.get('POSTGRES_PORT', '5432')
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
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/django_static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'django_static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "user.Custom_User"

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer"
    ],
    'DEFAULT_PAGINATION_CLASS': 'backend.__init__.Custom_Pagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

SPECTACULAR_SETTINGS = {
    'COMPONENT_SPLIT_REQUEST': True
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console']
        }
    }
}