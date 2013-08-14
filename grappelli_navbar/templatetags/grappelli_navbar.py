 #!/usr/bin/env python
 #-*- coding:utf-8 -*-

import sys

from django.conf import settings

from django import template

from classytags.helpers import InclusionTag


GRAPPELLI_NAVBAR = \
    getattr(settings, "GRAPPELLI_NAVBAR", u'grappelli_navbar.navbar.Navbar')

parts = GRAPPELLI_NAVBAR.split(".")
module = ".".join(parts[:-1])
__import__(module)
module = sys.modules[module]
Navbar = getattr(module, parts[-1])


def get_children(Navbar, request):
    children = []
    for node in Navbar.nodes:
        if node.__class__.__name__.endswith("Node"):
#            if isinstance(node, Node):
            title, params = node.as_tuple()
        else:
            title, params = node

        nodes = params.get("nodes", [])
        url = params.get('url')
        root = {'title': title, 'children': [], 'url': url}
        for node in nodes:
            if node.__class__.__name__.endswith("Node"):
#            if isinstance(node, Node):
                title, params = node.as_tuple()
            else:
                title, params = node

            url = params.get('url')
            perm = params.get('perm')
            node = {'title': title, 'url': url}
            if perm is None or request.user.has_perm(perm):
                root['children'].append(node)

        if root['children'] or root['url']:
            children.append(root)
    return children


class GrappelliNavbar(InclusionTag):
    name = u"grappelli_navbar"
    template = 'grappelli/navbar.html'

    def get_context(self, context):
        return {'children': get_children(Navbar, context['request'])}


register = template.Library()
register.tag(GrappelliNavbar)
