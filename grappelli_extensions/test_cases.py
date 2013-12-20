# -*- coding: utf-8 -*-

from django.template import Template, RequestContext
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from django.test import TestCase

from grappelli_extensions.templatetags.grappelli_navbar \
    import get_children, Navbar


class NavBarTestCase(TestCase):
    def setUp(self):
        login = 'root'
        email = 'root@local.host'
        password = 'pass123'
        self.user = User.objects.create_superuser(login, email, password)
        self.client = Client()
        self.client.login(username=login, password=password)

    def test_navbar_default(self):
        factory = RequestFactory()
        request = factory.get(reverse("admin:index"))
        request.user = self.user
        children = get_children(Navbar, request)

        self.assertEqual(len(children), 4)

        tpl = Template(u"{% load grappelli_navbar %}{% grappelli_navbar %}")
        self.assertTrue(len(tpl.render(RequestContext(request))) > 0)

    def test_navbar_admin_page(self):
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(len(response.context['children']), 4)
