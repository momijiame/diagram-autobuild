#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tempfile
import contextlib
import shutil


@contextlib.contextmanager
def tempdir():
    abspath = tempfile.mkdtemp()
    try:
        yield abspath
    finally:
        shutil.rmtree(abspath)
