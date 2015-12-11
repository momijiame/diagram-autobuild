#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import click
from livereload import Server
from livereload import shell

from diagram_autobuild.util import tempdir
from diagram_autobuild.tool import get_command
from diagram_autobuild.tool import get_tools
from diagram_autobuild.view import render
from diagram_autobuild.view import deploy


@click.command()
@click.option('--tool-opts', type=str,
              help='Options that are passed to the tool')
@click.option('--open-browser/--no-open-browser', default=True,
              help='Open your default browser when the command is executed')
@click.argument('tool', type=click.Choice(get_tools()))
@click.argument('source', type=click.Path(exists=True))
def cmd(tool_opts, open_browser, tool, source):
    with tempdir() as dirpath:
        server = Server()
        source_abspath = os.path.abspath(source)
        command_instance = get_command(tool, source_abspath, dirpath,
                                       tool_opts)
        command_str = str(command_instance)
        sh = shell(command_str, cwd=dirpath)
        sh()
        server.watch(source, sh)

        image_filepath = command_instance.destination
        image_filename = os.path.basename(image_filepath)

        page = render(image_filename)
        deploy(dirpath, page)

        server.serve(root=dirpath, open_url_delay=open_browser)


def main():
    cmd()


if __name__ == '__main__':
    main()
