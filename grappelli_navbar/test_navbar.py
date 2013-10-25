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
