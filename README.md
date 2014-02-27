# django-grappelli-extensions ![Navigation bar](https://api.travis-ci.org/gotlium/django-grappelli-navbar.png?branch=master)

#### Installation

 * Put ```grappelli_extensions``` **before** ```grappelli``` on INSTALLED_APPS
 * Put ```apptemplates.Loader``` on your TEMPLATE_LOADERS setting:

```python
# Your setting will look like:
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'apptemplates.Loader',
)

```

## navbar

![Navigation bar](https://github.com/gotlium/django-grappelli-navbar/raw/master/screenshot.jpg)

* Set the class that will generate your navigation bar:

```python
GRAPPELLI_EXTENSIONS_NAVBAR = 'navbar.Navbar'
```

## sidebar

![Navigation bar](https://github.com/gotlium/django-grappelli-navbar/raw/master/sidebar_screenshot.jpg)

* Set the class that will generate your sidebar:
```python
GRAPPELLI_EXTENSIONS_SIDEBAR = 'navbar.Sidebar'
```
#### navbar.py

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

**IMPORTANT:** Sidebar follows the very same structure.

## To run tests

```
python manage.py test --settings=grappelli_extensions.test_settings grappelli_extensions
```

## Contributing

1. Read the features ROADMAP
2. Fork it
3. Create your feature branch (`git checkout -b my-new-feature`)
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create new Pull Request :heart:


## Features

##### ROADMAP for 0.2

[ ] Static site with docs on github.io

[ ] Basic skins

[ ] Custom columns for Grappelli Dashboard

##### ROADMAP for 0.3

[ ] Customized icons for navbar

[ ] Customized icons for dashboard

##### ROADMAP for 0.4

[ ] Custom left sidebard
