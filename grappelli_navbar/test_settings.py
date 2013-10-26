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

    'grappelli_navbar',
    'grappelli',
    'django.contrib.admin',
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'apptemplates.Loader',
)

TEST_RUNNER = 'discover_runner.DiscoverRunner'
GRAPPELLI_NAVBAR = u'grappelli_navbar.test_navbar.Navbar'

ROOT_URLCONF = 'grappelli_navbar.test_urls'
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
