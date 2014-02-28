# django-grappelli-extensions ![Navigation bar](https://api.travis-ci.org/gotlium/django-grappelli-navbar.png?branch=master)

Available features:
* [Header navbar](#navbar)
* [Left sidebar](#sidebar)

#### Installation

```pip install django-grappelli-extensions``` and put ```grappelli_extensions``` **before** ```grappelli``` on INSTALLED_APPS.


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
python manage.py test --settings=grappelli_extensions.test_settings grappelli_extensions
```

## Contributing

1. Read the features ROADMAP.
2. Fork it.
3. Create your feature branch. (`git checkout -b my-new-feature`)
4. Commit your changes. (`git commit -am 'Add some feature'`)
5. Push to the branch. (`git push origin my-new-feature`)
6. Create new Pull Request.


## Features

##### ROADMAP for 0.1.2

[x] Custom left sidebard.

[ ] Make travis.yml file using grappelli-extensions account.

[ ] Static site on http://django-grappelli-extensions.github.io


##### ROADMAP for 0.1.3


[ ] Customized icons for navbar.

[ ] Customized icons for sidebar.

[ ] Customized icons for dashboard.


##### ROADMAP for 0.1.4

[ ] Create some skins themes.

[ ] Custom columns for Grappelli Dashboard.


##### ROADMAP for 0.1.5

[ ] Redesign Grappelli Dashboard.
