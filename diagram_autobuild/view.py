#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from jinja2 import Environment
from jinja2 import PackageLoader


def render(imgpath):
    loader = PackageLoader('diagram_autobuild', 'templates')
    env = Environment(loader=loader)
    template = env.get_template('index.html')
    page = template.render(imgpath=imgpath)
    return page


def deploy(dirpath, text):
    filepath = os.path.join(dirpath, 'index.html')
    with open(filepath, mode='w') as f:
        f.write(text)
