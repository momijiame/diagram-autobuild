#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest

from diagram_autobuild.tool import GraphvizBuild
from diagram_autobuild.tool import BlockdiagBuild
from diagram_autobuild.tool import NwdiagBuild
from diagram_autobuild.tool import SeqdiagBuild
from diagram_autobuild.tool import ActdiagBuild


class Test_GraphvizBuild(object):

    def test(self):
        src_file = '/foo/sample.dot'
        dst_dir = '/bar'
        build = GraphvizBuild(src_file, dst_dir)

        expect_path = '/bar/out.png'
        assert build.destination == expect_path

        expect_command = 'dot  -T png -o /bar/out.png /foo/sample.dot'
        assert str(build) == expect_command


class Test_BlockdiagSeriesBuild(object):

    @pytest.mark.parametrize(('command_name', 'class_'), [
        ('blockdiag', BlockdiagBuild),
        ('nwdiag', NwdiagBuild),
        ('seqdiag', SeqdiagBuild),
        ('actdiag', ActdiagBuild),
    ])
    def test(self, command_name, class_):
        src_file = '/foo/sample.diag'
        dst_dir = '/bar'
        build = class_(src_file, dst_dir)

        expect_path = '/bar/out.png'
        assert build.destination == expect_path

        expect_command = '{cmd}  -o /bar/out.png /foo/sample.diag'.format(
            cmd=command_name,
        )
        assert str(build) == expect_command


if __name__ == '__main__':
    pytest.main()
