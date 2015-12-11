#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import os

from future.utils import with_metaclass


class BuildCommand(with_metaclass(abc.ABCMeta)):

    def __init__(self, src_file, dst_dir, opts=None):
        self.src_file = src_file
        self.dst_dir = dst_dir
        self.opts = opts or ''

    @abc.abstractproperty
    def destination(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass


class GraphvizBuild(BuildCommand):

    @property
    def destination(self):
        return os.path.join(self.dst_dir, 'out.png')

    def __str__(self):
        command = 'dot {opts} -T png -o {destination} {src_file}'.format(
            destination=self.destination,
            src_file=self.src_file,
            opts=self.opts,
        )
        return command


class BlockdiagSeriesBuild(BuildCommand):

    @abc.abstractproperty
    def command(self):
        pass

    @property
    def destination(self):
        return os.path.join(self.dst_dir, 'out.png')

    def __str__(self):
        command = '{command} {opts} -o {destination} {src_file}'.format(
            command=self.command,
            destination=self.destination,
            src_file=self.src_file,
            opts=self.opts,
        )
        return command


class BlockdiagBuild(BlockdiagSeriesBuild):

    @property
    def command(self):
        return 'blockdiag'


class NwdiagBuild(BlockdiagSeriesBuild):

    @property
    def command(self):
        return 'nwdiag'


class SeqdiagBuild(BlockdiagSeriesBuild):

    @property
    def command(self):
        return 'seqdiag'


class ActdiagBuild(BlockdiagSeriesBuild):

    @property
    def command(self):
        return 'actdiag'


_MAPPINGS = {
    'graphviz': GraphvizBuild,
    'blockdiag': BlockdiagBuild,
    'nwdiag': NwdiagBuild,
    'seqdiag': SeqdiagBuild,
    'actdiag': ActdiagBuild,
}


def get_tools():
    return _MAPPINGS.keys()


def get_command(tool_name, src_file, dst_dir, opts=None):
    class_ = _MAPPINGS.get(tool_name)
    instance = class_(src_file, dst_dir, opts)
    return instance
