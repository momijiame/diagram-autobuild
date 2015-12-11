#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

import pytest

from diagram_autobuild.util import tempdir


class Test_tempdir(object):

    def test(self):
        """ 使い終わった一時ディレクトリが削除される """
        with tempdir() as dirpath:
            assert type(dirpath) == str

        assert not os.path.exists(dirpath)

    def test_when_exception(self):
        """ ブロック内で例外が発生しても一時ディレクトリが削除される """
        with pytest.raises(Exception):
            with tempdir() as dirpath:
                raise Exception('Oops!')

        assert not os.path.exists(dirpath)

    def test_delete_files(self):
        """ 一時ディレクトリ内にファイルがあってもディレクトリごと削除される """
        with tempdir() as dirpath:
            filepath = os.path.join(dirpath, 'temporary.txt')
            with open(filepath, 'wb') as f:
                f.write(b'Hello, World!')

        assert not os.path.exists(dirpath)


if __name__ == '__main__':
    pytest.main()
