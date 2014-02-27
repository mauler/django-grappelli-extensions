DATABASE_ENGINE = 'sqlite3'

SITE_ID = 1

SECRET_KEY = '52b700e3a9dc3f83a410df37777fefbc'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'grappelli_extensions',
    'grappelli',
    'django.contrib.admin',
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'apptemplates.Loader',
)

GRAPPELLI_EXTENSIONS_NAVBAR = 'grappelli_extensions.test_navbar.Navbar'
GRAPPELLI_EXTENSIONS_SIDEBAR = 'grappelli_extensions.test_navbar.Sidebar'

ROOT_URLCONF = 'grappelli_extensions.test_urls'
STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
)


'''
The confs bellow are used when for some reason the grappelli wasn't installed
by PIP, lets say in a development env.
'''
import os
import sys

PROJECT_PATH = ORIGINAL_PROJECT_PATH = \
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_PATH)
