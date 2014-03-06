# django-grappelli-navbar

![Navigation bar](https://api.travis-ci.org/gotlium/django-grappelli-navbar.png?branch=master)


![Navigation bar](https://github.com/gotlium/django-grappelli-navbar/raw/master/screenshot.jpg)


# settings.py

 * Put 'grappelli_navbar' **before** 'grappelli' on INSTALLED_APPS
 * Put 'apptemplates.Loader' on your TEMPLATE_LOADERS setting:

```python
# Your setting will look like:
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'apptemplates.Loader',
)

```
 * Set the class that will generate your navigation bar:

```python
GRAPPELLI_NAVBAR = 'navbar.Navbar'
```

# navbar.py

```python
from django.core.urlresolvers import reverse_lazy

from grappelli_navbar.nodes import CLNode


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

## CHANGELOG

### 0.2.0 (2 Dec, 2013)
#### Improvements:
* Adds param "perms" to CLNode (Accept a list of admin permissions ex: ['change', 'add'] and if any of these is valid the node is showed)


## TODO

[x] Close dropdown when other is clicked.

[ ] Create helper roots: AppRoot

[ ] Create helper nodes: AppNode, ModelNode

