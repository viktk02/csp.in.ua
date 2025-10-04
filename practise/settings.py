from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.getenv('SECRET_KEY')

ADMIN_TWO_FACTOR_NAME = 'BT_VERIFICATION'
TWO_FACTOR_QR_FACTORY = 'qrcode.image.pil.PilImage'
CSP_IMG_SRC = ("'self'", "data:", "https:") 

DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['csp.in.ua','www.csp.in.ua', 'localhost',
    '127.0.0.1', ]

INSTALLED_APPS = [
    'admin_two_factor.apps.TwoStepVerificationConfig',
    'django_ckeditor_5',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
    'main',
    'csp',
    'axes',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
    'axes.middleware.AxesMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'practise.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processor.current_year'

            ],
        },
    },
]

WSGI_APPLICATION = 'practise.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
        'ATOMIC_REQUESTS': True,
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

LANGUAGE_CODE = 'uk-UA'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('uk', 'Ukrainian'),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #different from production

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CKEDITOR_5_UPLOAD_FILE = True
CKEDITOR_5_UPLOAD_IMAGE = True
CKEDITOR_5_CUSTOM_CSS = 'css/ckeditor-content.css'

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|',
            'bold', 'italic', 'link', 'underline', '|',
            'bulletedList', 'numberedList', 'blockQuote', '|',
            'imageUpload', 'mediaEmbed', '|',
            'undo', 'redo'
        ],
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
            ]
        },
        'image': {
            'toolbar': [
                'imageTextAlternative', '|',
                'imageResize'
            ],
        },
        'mediaEmbed': {
            'previewsInData': True,
        },
        'contentCss': [
            '/static/ckeditor/ckeditor/styles/content.css'
        ],
    },
}

CONTENT_SECURITY_POLICY = {
    "DIRECTIVES": {
        "default-src": ["'self'"],
        "script-src": [
            "'self'",
            "https://www.youtube.com",
            "https://s.ytimg.com"
        ],
        "style-src": [
            "'self'",
            "https://fonts.googleapis.com"
        ],
        "img-src": [
            "'self'",
            "data:",
            "https://i.ytimg.com",
            "https://*.ytimg.com"
        ],
        "frame-src": [
            "'self'",
            "https://www.youtube.com",
            "https://youtube.com"
        ],
        "media-src": [
            "'self'",
            "https://www.youtube.com",
            "https://youtube.com"
        ],
        "font-src": [
            "'self'",
            "https://fonts.gstatic.com"
        ],
        "connect-src": ["'self'"]
    }
}