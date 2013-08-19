#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pprint import pprint

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from django.template import Template, RequestContext
from django.test.client import RequestFactory

from grappelli_navbar.templatetags.grappelli_navbar import get_children, Navbar


class Command(BaseCommand):
    help = "Outputs grappelli-navbar."

    def handle(self, *args, **options):
        factory = RequestFactory()
        url = reverse("admin:index")
        request = factory.get(url)
        request.user = User.objects.filter(is_superuser=True)[:1].get()
        children = get_children(Navbar, request)
        pprint(children)
        template = Template(
            u"{% load grappelli_navbar %}{% grappelli_navbar %}")
        print template.render(RequestContext(request))
