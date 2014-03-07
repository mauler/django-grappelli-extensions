 #-*- coding:utf-8 -*-

import sys

from django import template
from django.conf import settings
from django.templatetags.static import static

from classytags.core import Tag, Options
from classytags.helpers import InclusionTag


def get_extension(setting, default, *args, **kwargs):
    extension = getattr(settings, setting, default)
    parts = extension.split(".")
    module = ".".join(parts[:-1])
    __import__(module)
    module = sys.modules[module]
    return getattr(module, parts[-1])


def get_navbar():
    return get_extension('GRAPPELLI_EXTENSIONS_NAVBAR',
                         'grappelli_extensions.navbar.Navbar')


def get_sidebar():
    return get_extension('GRAPPELLI_EXTENSIONS_SIDEBAR',
                         'grappelli_extensions.navbar.Navbar')


def get_theme():
    return getattr(settings, 'GRAPPELLI_THEME', None)


def has_perms(request, params):
    if 'perm' in params:
        perms = [params['perm']]
    else:
        perms = params.get('perms', [])
    if perms:
        perms = [request.user.has_perm(p) for p in perms]
        return any(perms)
    return True


def get_children(Navbar, request):
    children = []
    for node in Navbar.nodes:
        if node.__class__.__name__.endswith("Node"):
            title, params = node.as_tuple()
        else:
            title, params = node

        if not has_perms(request, params):
            continue

        nodes = params.get("nodes", [])
        url = params.get('url')
        root = {'title': title, 'children': [], 'url': url}
        for node in nodes:
            if node.__class__.__name__.endswith("Node"):
                title, params = node.as_tuple()
            else:
                title, params = node

            url = params.get('url')
            node = {'title': title, 'url': url}
            if has_perms(request, params):
                root['children'].append(node)

        if root['children'] or root['url']:
            children.append(root)
    return children


class GrappelliNavbar(InclusionTag):
    name = 'grappelli_navbar'
    template = 'grappelli/navbar.html'

    def get_context(self, context):
        navbar = get_navbar()
        return {'children': get_children(navbar, context['request'])}


class GrappelliSidebar(InclusionTag):
    name = 'grappelli_sidebar'
    template = 'grappelli/sidebar.html'

    def get_context(self, context):
        sidebar = get_sidebar()
        return {
            'sidebar_children': get_children(sidebar, context['request']),
            'request': context['request']
        }


class GrappelliHasSidebar(Tag):
    name = 'grappelli_has_sidebar'
    options = Options(
        blocks=[('endsidebar', 'nodelist')],
    )

    def render_tag(self, context, nodelist):
        output = ''
        sidebar = get_sidebar()
        if(len(sidebar.nodes)):
            output = nodelist.render(context)
        return output


class GrappelliTheme(Tag):
    name = 'grappelli_theme'

    def render_tag(self, context):
        theme = get_theme()
        if not theme:
            return ''

        theme_static_url = static('css/%s.css' % (theme, ))
        output = '<link href=%s rel="stylesheet" type="text/css"\
                 media="screen" />' % (theme_static_url, )
        return output


register = template.Library()
register.tag(GrappelliNavbar)
register.tag(GrappelliSidebar)
register.tag(GrappelliHasSidebar)
register.tag(GrappelliTheme)
