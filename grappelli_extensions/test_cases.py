# -*- coding: utf-8 -*-

from django.template import Template, RequestContext
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from django.test.utils import override_settings
from django.test import TestCase

from grappelli_extensions.templatetags.grappelli_navbar \
    import get_children, get_navbar, get_sidebar


class BaseTestCase(TestCase):
    def setUp(self):
        login = 'root'
        email = 'root@local.host'
        password = 'pass123'
        self.user = User.objects.create_superuser(login, email, password)
        self.client = Client()
        self.client.login(username=login, password=password)


class NavBarTestCase(BaseTestCase):
    def test_navbar_default(self):
        factory = RequestFactory()
        request = factory.get(reverse("admin:index"))
        request.user = self.user
        navbar = get_navbar()
        children = get_children(navbar, request)

        self.assertEqual(len(children), 4)

        tpl = Template(u"{% load grappelli_navbar %}{% grappelli_navbar %}")
        self.assertTrue(len(tpl.render(RequestContext(request))) > 0)

    def test_navbar_admin_page(self):
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(len(response.context['children']), 4)


class SideBarTestCase(BaseTestCase):
    def test_sidebar_default(self):
        factory = RequestFactory()
        request = factory.get(reverse("admin:index"))
        request.user = self.user
        sidebar = get_sidebar()
        children = get_children(sidebar, request)

        self.assertEqual(len(children), 3)

        tpl = Template(u"{% load grappelli_navbar %}{% grappelli_sidebar %}")
        self.assertTrue(len(tpl.render(RequestContext(request))) > 0)

    def test_sidebar_admin_page(self):
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(len(response.context['sidebar_children']), 3)


@override_settings(GRAPPELLI_EXTENSIONS_SIDEBAR=
                   'grappelli_extensions.navbar.Navbar')
class NoSideBarTestCase(BaseTestCase):
    def test_no_sidebar_admin_page(self):
        factory = RequestFactory()
        request = factory.get(reverse("admin:index"))
        request.user = self.user
        tpl = Template(u"{% load grappelli_navbar %}"
                       "{% grappelli_has_sidebar %}"
                       "{% grappelli_sidebar %}"
                       "{% endsidebar %}")
        self.assertFalse(len(tpl.render(RequestContext(request))))
