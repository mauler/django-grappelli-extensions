#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import re
import sys


VERSION_FILE = 'grappelli_navbar/__init__.py'
version_text = open(VERSION_FILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, version_text, re.M)
if mo:
    version = mo.group(1)
else:
    raise RuntimeError(
        "Unable to find version string in %s." % (VERSION_FILE,))


name = 'django-grappelli-navbar'
package = 'grappelli_navbar'
description = u'Navigation bar on Django administration'
url = 'http://github.com/mauler/django-grappelli-navbar'
author = 'Paulo Roberto Macedo Chaves'
author_email = 'proberto.macedo@gmail.com'
license = 'BSD'
install_requires = [
    'django-apptemplates>=0.0.1',
    'django-grappelli>=2.4.7',
    'django-classy-tags>=0.4']


if sys.argv[-1] == 'publish':
    code = os.system("python setup.py sdist upload")
    if code:
        sys.exit()

    args = {'version': version}
    print "You probably want to also tag the version now:"
    print "  git tag -a %(version)s -m 'version %(version)s'" % args
    print "  git push --tags"
    sys.exit()


setup(
    name=name,
    version=version,
    url=url,
    author=author,
    author_email=author_email,
    license=license,
    packages=find_packages(),
    include_package_data=True,
    description=description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
    install_requires=install_requires
)
