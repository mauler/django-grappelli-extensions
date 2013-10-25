# django-grappelli-navbar

![Navigation bar](https://github.com/gotlium/django-grappelli-navbar/raw/master/screenshot.jpg)


## Requirements

 * django-apptemplates
```sh
pip install django-apptemplates
```


# settings.py

 * Put 'grappelli_navbar' before 'grappelli' on INSTALLED_APPS
 * Put 'apptemplates.Loader' no your TEMPLATE_LOADERS setting:

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
GRAPPELLI_NAVBAR = u'navbar.Navbar'
```

# navbar.py

```python
#-*- coding:utf-8 -*-

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


## TODO

[ ] Close dropdown when other is clicked.

[ ] Create helper roots: AppRoot

[ ] Create helper nodes: AppNode, ModelNode
