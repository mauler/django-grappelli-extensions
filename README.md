# django-grappelli-extensions

[![Test Status](https://travis-ci.org/mauler/django-grappelli-extensions.png?branch=master)](https://travis-ci.org/mauler/django-grappelli-extensions)

[![Code Health](https://landscape.io/github/mauler/django-grappelli-extensions/master/landscape.png)](https://landscape.io/github/mauler/django-grappelli-extensions/master)

[![Latest PyPI version](https://pypip.in/v/django-grappelli-extensions/badge.png)](https://crate.io/packages/django-grappelli-extensions/)

[![Number of PyPI downloads](https://pypip.in/d/django-grappelli-extensions/badge.png)](https://crate.io/packages/django-grappelli-extensions/)


Available features:
* [Header navbar](#navbar)
* [Left sidebar](#sidebar)

* Python > 2.6
* django-grappelli >= 2.4.5
* Django >= 1.4

# Installation

* ```pip install django-grappelli-extensions```
* Put ```grappelli_extensions``` **before** ```grappelli``` on INSTALLED_APPS.


## settings.py

 * Put 'grappelli_extensions' **before** 'grappelli' on INSTALLED_APPS
 * Put 'apptemplates.Loader' on your TEMPLATE_LOADERS setting:

```python
# Your setting will look like:
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'apptemplates.Loader',
)
```

![Navigation bar](https://github.com/mauler/django-grappelli-extensions/raw/master/screenshot.jpg)

Set the class that will generate your navigation bar:

```python
GRAPPELLI_EXTENSIONS_NAVBAR = 'extensions.Navbar'
```
or if you have multiple admin sites
```python
GRAPPELLI_EXTENSIONS_NAVBAR = {  # alternative method
    'yourproject.admin.admin_site': 'yourproject.extensions.Navbar',
    'yourproject.admin.second_admin_site': 'yourproject.extensions.second_Navbar',
}
```

## sidebar

![Navigation bar](https://github.com/mauler/django-grappelli-extensions/raw/master/sidebar_screenshot.jpg)

Set the class that will generate your sidebar:
```python
GRAPPELLI_EXTENSIONS_SIDEBAR = 'extensions.Sidebar'
```
or if you have multiple admin sites
```python
GRAPPELLI_EXTENSIONS_SIDEBAR = {  # alternative method
    'yourproject.admin.admin_site': 'yourproject.extensions.Sidebar',
    'yourproject.admin.second_admin_site': 'yourproject.extensions.second_Sidebar',
}
```

#### extensions.py

```python
from django.core.urlresolvers import reverse_lazy

from grappelli_extensions.nodes import CLNode


class Navbar(object):
    nodes = (
        ('Auth', {'nodes': (
            ('Users', {
                'url': reverse_lazy('admin:auth_user_changelist'),
                'perm': 'auth.change_user',
            }),
            ('Groups', {
                'url': reverse_lazy('admin:auth_group_changelist'),
                'perm': 'auth.change_group',
            }),
        )}),
        ('Sites',
            {'url': reverse_lazy('admin:sites_site_changelist')}),
        ('Nodes', {'nodes': (
            CLNode('auth', 'user'),
            CLNode('sites', 'site'),
        )}),
        CLNode('auth', 'user', u"Site users"),
    )
```

**IMPORTANT:** Sidebar class follows the very same structure (But only use root nodes).

## To run tests

```
pip install -r requirements/tests.txt Django
export DJANGO_SETTINGS_MODULE=grappelli_extensions.test_settings
`which django-admin.py` test grappelli_extensions"
```

## Contributing

1. Fork it.
2. Create your feature branch. (`git checkout -b my-new-feature`)
3. Commit your changes. (`git commit -am 'Add some feature'`)
4. Push to the branch. (`git push origin my-new-feature`)
5. Create new Pull Request.
