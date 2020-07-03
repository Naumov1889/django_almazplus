import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = []

# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'adminsortable2',
    'ckeditor',
    'ckeditor_uploader',
    'constance',
    'constance.backends.database',
    'django_cleanup.apps.CleanupConfig',
]

LOCAL_APPS = [
    'base',
    'callback',
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

                'constance.context_processors.config',
                'base.context_processors.callback',
                'base.context_processors.contact'
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [['Source', '-', 'Save', 'NewPage', 'Preview', '-'],
                    ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
                    ['Find', 'Replace', '-', 'SelectAll', '-'],
                    ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting',
                     'RemoveFormat'],
                    ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                     'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-'],
                    ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'],
                    ['Link', 'Unlink', 'Anchor'],
                    ['Styles', 'Format', 'Font', 'FontSize'], ['TextColor', 'BGColor'], ['Maximize', 'ShowBlocks'],
                    ],
        'height': 600,
        'width': 1000
        # 'toolbar': None,
        # 'enterMode': 2,
        # 'shiftEnterMode': 3
    },

}

CKEDITOR_UPLOAD_PATH = "uploads/"

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True

CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': ['django.forms.ImageField', {}]
}

CONSTANCE_CONFIG = {
    'TITLE_1': ('Наша продукция', 'Наша продукция'),
    'TITLE_2': ('Вакансии', 'Вакансии'),
    'TITLE_3': ('Политика конфиденциальности', 'Политика конфиденциальности'),
    'TITLE_4': ('Пользовательское соглашение', 'Пользовательское соглашение'),
    'TITLE_5': ('Контакты', 'Контакты'),
    'TITLE_6': ('О компании', 'О компании'),
    'CALLBACK_TITLE': ('Хотите заказать или есть другие вопросы?', ''),
    'CALLBACK_SUBTITLE': (
        'Оставьте свои контакты, наш менеджер свяжется с вами в течении 15 минут и ответит на ваши вопросы', ''),
    'LOGO_IMG': ('logo-almaz.png', 'Лого картинка', 'image_field'),
    'LOGO_TEXT': ('АЛМАЗ', 'Лого текст'),
    'ABOUT_PAGE_MAP_BG': ('bg-map.jpg', 'Фавиконка', 'image_field'),
    'FAVICON': ('favicon.ico', 'Фавиконка', 'image_field'),
    'AUTHOR': ('Разработка сайта <a href="https://rfim.ru/">rfim.ru</a>', 'Автор',),
    'COPYRIGHT': ('© Все права защищены. 2020', 'Копирайт',),
}
