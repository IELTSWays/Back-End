from os import environ
from pathlib import Path
from urllib.parse import quote


# GET ENV UTIL
def get_env(key, default=None, optinal=False):
    """Return environment variables with some options."""
    val = environ.get(key)
    if val is not None:
        return val
    elif default is not None:
        return default
    elif not optinal:
        raise ValueError(f"Environment variable {key} was not defined")
# END GET ENV UTIL


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SITE_ID = 2

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


# APP CONFIGURATION
DJANGO_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.admindocs",
)

THIRD_PARTY_APPS = (
    "rest_framework",
    "django_filters",
    "corsheaders",
    "gunicorn",
    "django.contrib.sites",
    "ckeditor",
    "ckeditor_uploader",
    "oauth2_provider",
    "social_django",
    "drf_social_oauth2",
    "storages",
    "dropbox",
    "whitenoise",
    "dbbackup",
)

# Apps specific for this project go here.

LOCAL_APPS = (
    "accounts",
    "ticket",
    "city",
    "book",
    "exam",
    "order",
    "teacher",
    "answers",
    "report",
)


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates/",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


ACCOUNT_EMAIL_VERIFICATION = "none"


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation"
            ".UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.NumericPasswordValidator"
        ),
    },
]
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True



'''
DEFAULT_FILE_STORAGE = "storages.backends.dropbox.DropboxStorage"
STATICFILES_STORAGE = "storages.backends.dropbox.DropboxStorage"
DROPBOX_OAUTH2_TOKEN = 'sl.B0QgKhXh9pTYG2vtkLwr80zpLEqcRSFthu0h9qAhQYVrNHlH2KPIHRhxcnLkZ2wujHIfr6HvwSuuVMjM1tbe-RxMm-Vbvv42hagyW5Acag0bA_l_TgX8CzdkEJOUaZhN8PNGnJm5eAym'
DROPBOX_ROOT_PATH = '/'
DROPBOX_APP_KEY = "qvnub2a1xi9x0cf"
DROPBOX_APP_SECRET = "n2sn1aat2h7llu8"
DROPBOX_OAUTH2_REFRESH_TOKEN = "w63Sx2mDljAAAAAAAAABfV0gcdxkSiBESjvMUcMia70"
DROPBOX_refresh_token = "w63Sx2mDljAAAAAAAAABfV0gcdxkSiBESjvMUcMia70"
DROPBOX_access_token = "sl.B0QgKhXh9pTYG2vtkLwr80zpLEqcRSFthu0h9qAhQYVrNHlH2KPIHRhxcnLkZ2wujHIfr6HvwSuuVMjM1tbe-RxMm-Vbvv42hagyW5Acag0bA_l_TgX8CzdkEJOUaZhN8PNGnJm5eAym"
DROPBOX_AUTHORIZATION_CODE = "w63Sx2mDljAAAAAAAAABfV0gcdxkSiBESjvMUcMia70"
DROPBOX_TIMEOUT = 100
DROPBOX_WRITE_MODE = "add"
DROPBOX_ACCESS_TOKEN = "sl.B0QgKhXh9pTYG2vtkLwr80zpLEqcRSFthu0h9qAhQYVrNHlH2KPIHRhxcnLkZ2wujHIfr6HvwSuuVMjM1tbe-RxMm-Vbvv42hagyW5Acag0bA_l_TgX8CzdkEJOUaZhN8PNGnJm5eAym"

STORAGES = {
    'default': {
        'BACKEND': 'storages.backends.dropbox.DropboxStorage',
        'OPTIONS': {
            'access_token': DROPBOX_ACCESS_TOKEN,
            'root_path': DROPBOX_ROOT_PATH,
            'timeout': DROPBOX_TIMEOUT,
        },
    },
}
'''



# S3 Settings
LIARA_ENDPOINT="https://storage.iran.liara.space"
LIARA_BUCKET_NAME="ieltsways2"
LIARA_ACCESS_KEY="lthvqv95sq0ar3u2"
LIARA_SECRET_KEY="3a3d8ffa-fcc5-45e1-a81f-b4c0c8ff2177"

# S3 Settings Based on AWS (optional)
AWS_ACCESS_KEY_ID = LIARA_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = LIARA_SECRET_KEY
AWS_STORAGE_BUCKET_NAME = LIARA_BUCKET_NAME
AWS_S3_ENDPOINT_URL = LIARA_ENDPOINT
AWS_S3_REGION_NAME = 'us-east-1'

# Django-storages configuration
STORAGES = {
  "default": {
      "BACKEND": "storages.backends.s3.S3Storage",
  },
  "staticfiles": {
      "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
  },
}



DBBACKUP_STORAGE = 'storages.backends.s3.S3Storage'
DBBACKUP_STORAGE_OPTIONS = {'location': 'dbbackup/'}
DBBACKUP_CLEANUP_KEEP = 7






# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = get_env("STATIC_ROOT", default="/static/")
STATIC_URL = get_env("STATIC_URL", default="/static/")
MEDIA_ROOT = "https://ieltsways2.storage.iran.liara.space/media/"
MEDIA_URL = "https://ieltsways2.storage.iran.liara.space/media/"
static_file_env = get_env("STATICFILES_DIRS", optinal=True)

STATICFILES_DIRS = (
    static_file_env.split(",") if static_file_env is not None else ["docs/"]
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# CACHING CONFIGURATION
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        #"LOCATION": get_env("REDIS_URL"),
        "LOCATION": "redis://195.214.235.46:6379/1",
    }
}
# END CACHING CONFIGURATION

# AUTH USER MODEL CONFIGURATION
AUTH_USER_MODEL = "accounts.User"
# END AUTH USER MODEL CONFIGURATION

# OTP CONFIGURATION
OTP_CODE_LENGTH = int(get_env("OTP_CODE_LENGTH", default="4"))
OTP_TTL = int(get_env("OTP_TTL", default="120"))
# END OTP CONFIGURATION

# JWT SETIINGS
ACCESS_TTL = int(get_env("ACCESS_TTL", default="1"))  # days
REFRESH_TTL = int(get_env("REFRESH_TTL", default="2"))  # days
# END JWT SETTINGS




'''
AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'drf_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]
'''
# Google Configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "366111965494-bbgflimp8s9dtndoufsah3v235bt8lhh.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"

# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]



# REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "accounts.backends.JWTAuthentication",
        #"rest_framework.authentication.TokenAuthentication",
        #"rest_framework.authentication.SessionAuthentication",
        #"oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        #"drf_social_oauth2.authentication.SocialAuthentication",
    ),
    "DEFAULT_THROTTLE_RATES": {"otp": get_env("OTP_THROTTLE_RATE", default="10/min"), },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# END REST FRAMEWORK CONFIGURATION

MAX_UPLOAD_SIZE = 5242880

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Format', 'Font', 'FontSize'],
            ['Bold', 'Italic'],
            ['TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList'],
            ['Image', 'Flash', 'Table'],
            ['Source']
        ],
        'height': 100,
        'width': 650
    }
}



# CORSHEADERS CONFIGURATION
ALLOWED_HOSTS = ['195.214.235.46','localhost','127.0.0.1','0.0.0.0', 'ieltsways.com']
CORS_ALLOWED_ORIGINS = ["https://.ieltsways.com", "https://api.ieltsways.com", "http://195.214.235.46", "http://localhost", "http://127.0.0.1", "https://ieltsways.com", "https://ioc.ieltsways.com"]
CSRF_TRUSTED_ORIGINS = ["https://.ieltsways.com", "https://api.ieltsways.com", "http://195.214.235.46", "http://localhost", "http://127.0.0.1", "https://ieltsways.com", "https://ioc.ieltsways.com"]
CORS_ORIGIN_ALLOW_ALL = True
CORS_REPLACE_HTTPS_REFERER = True
CORS_ALLOW_CREDENTIALS = True
#SESSION_COOKIE_SECURE=True
#CSRF_COOKIE_SECURE = False
#CSRF_COOKIE_HTTPONLY = False
#SESSION_COOKIE_SAMESITE = False
#SESSION_COOKIE_DOMAIN = "http://195.214.235.46"
#CORS_ORIGIN_WHITELIST = ["http://195.214.235.46:8000", "http://195.214.235.46", "http://localhost", "http://127.0.0.1", "https://195.214.235.46"]
# END CORSHEADERS CONFIGURATION



# SMS CONFIGURATION
KAVENEGAR_API_KEY = "7572365451704156594870726D765276525A7468646D553857503161754D683669545A6D755748517658383D"
KAVENEGAR_TEMPLATE = "otp-verify"
# END SMS CONFIGURATION

APPEND_SLASH = True


# ZARRINPAL CONFIGURATION
SANDBOX = True
ZARRINPAL_URL="https://api.zarinpal.com/pg/"
#ZARRINPAL_MERCHANT_ID = "a5e628f8-4d52-47c9-83f1-01cf80c2bb42"
ZARRINPAL_MERCHANT_ID = "00000000-0000-0000-0000-000000000000"
ZP_API_REQUEST = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/"
ZARIN_CALL_BACK = 'https://api.ieltsways.com/order/zarinpal-verify/'
REPORT_ZARIN_CALL_BACK = 'https://api.ieltsways.com/report/full-report-verify/'
MEDIA_REPORT_ZARIN_CALL_BACK = 'https://api.ieltsways.com/report/media-report-verify/'
ZARIN_SPEAKING_CALL_BACK = 'https://api.ieltsways.com/order/zarinpal-speaking-verify/'
ZARIN_WRITING_CALL_BACK = 'https://api.ieltsways.com/order/zarinpal-writing-verify/'
# END ZARRINPAL CONFIGURATION



# ZIBAL CONFIGURATION
ZIBAL_MERCHANT_ID = "65a69be3c5d2cb0011fa9141"
ZIBAL_CALL_BACK = 'https://api.ieltsways.com/order/payment-verify/'
# END ZIBAL CONFIGURATION
