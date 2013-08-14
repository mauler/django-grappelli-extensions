# django-grappelli-navbar

## Requirements

 * django-apptemplates
 ```sh
pip install django-apptemplates
```


# settings.py

 * Put 'grappelli_navbar' before 'grappelli' on INSTALLED_APPS

 * Set the class that will generate your navigation bar.

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
        (u'Permissões', {'nodes': (
            (u'Usuários', {
                'url': reverse_lazy('admin:auth_user_changelist'),
                'perm': 'auth.change_user',
            }),
            (u'Grupos', {
                'url': reverse_lazy('admin:auth_group_changelist'),
                'perm': 'auth.change_group',
            }),
        )}),
        (u'Equipamentos',
            {'url': reverse_lazy('admin:core_tablet_changelist')}),
        (u'Cadastros', {'nodes': (
            CLNode('core', 'projeto'),
            CLNode('core', 'area'),
        )}),
        CLNode('core', 'campanha', u"Agenda"),
    )
```


## TODO

[ ] Screenshots on README.md

[ ] Close dropdown when other is clicked.

[ ] setup.py

[ ] Create helper roots: AppRoot

[ ] Create helper nodes: AppNode, ModelNode
