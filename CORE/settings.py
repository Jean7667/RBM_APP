
import os
from pathlib import Path
from decouple import config
import dj_database_url
import django_on_heroku

#https://pypi.org/project/django-on-heroku/


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_extensions',
    'user_app',
    'debug_toolbar',
    'django_on_heroku'
]



AUTH_USER_MODEL = 'user_app.CustomUser' #customer user

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'CORE.urls'


LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

TEMPLATES = [
    {
       "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS":  [TEMPLATES_DIR],
        "APP_DIRS": True,
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

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_FAIL_SILENTLY = False

WSGI_APPLICATION = 'CORE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
 """

# Use dj_database_url to configure the database
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / "staticfiles"



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



""" LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Define console handler
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        # Define file handler
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),  # Specify log file path
        },
    },
    'loggers': {
        # Root logger
        '': {
            'handlers': ['console', 'file'],  # Log to both console and file
            'level': 'DEBUG',
        },
        # Django logger
        'django': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}  """
 
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
] 

django_on_heroku.settings(locals())