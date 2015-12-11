#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

import pytest

from diagram_autobuild.view import render
from diagram_autobuild.view import deploy


class Test_render(object):

    def test(self):
        imgpath = 'sample.png'
        page = render(imgpath)

        assert page.find(imgpath) != -1


class Test_deploy(object):

    def test(self, tmpdir):
        text = 'Hello, World!'
        dirpath = tmpdir.dirname
        deploy(dirpath, text)

        filepath = os.path.join(dirpath, 'index.html')
        with open(filepath, mode='r') as f:
            result = f.read()

        assert text == result


if __name__ == '__main__':
    pytest.main('-s')
