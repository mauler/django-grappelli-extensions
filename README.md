# django-grappelli-extensions [![Build Status](https://travis-ci.org/django-grappelli-extensions/django-grappelli-extensions.png?branch=master)](https://travis-ci.org/django-grappelli-extensions/django-grappelli-extensions)


Available features:
* [Header navbar](#navbar)
* [Left sidebar](#sidebar)

#### Installation

* Python 2.6, 2.7, django-grappelli >= 2.4.5 and Django >= 1.4
* Simply ```pip install django-grappelli-extensions``` and put ```grappelli_extensions``` **before** ```grappelli``` on INSTALLED_APPS.


## navbar

![Navigation bar](https://github.com/django-grappelli-extensions/django-grappelli-extensions/raw/master/screenshot.jpg)

Set the class that will generate your navigation bar:

```python
GRAPPELLI_EXTENSIONS_NAVBAR = 'extensions.Navbar'
```

## sidebar

![Navigation bar](https://github.com/django-grappelli-extensions/django-grappelli-extensions/raw/master/sidebar_screenshot.jpg)

Set the class that will generate your sidebar:
```python
GRAPPELLI_EXTENSIONS_SIDEBAR = 'extensions.Sidebar'
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

**IMPORTANT:** Sidebar class follows the very same structure.

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
