#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages
from pip.req import InstallRequirement


def _exclude_conditions():
    return {}


def _is_exclude(project_name):
    conditions = _exclude_conditions()

    condition_info = conditions.get(project_name)
    if condition_info is None:
        # パッケージの情報が登録されていなければインストールする
        return False

    # 除外対象か否かの情報を返す
    return condition_info


def _line2project_name(line):
    install_requirement = InstallRequirement.from_line(line)
    requirement_parse = install_requirement.req
    return requirement_parse.project_name


def _load_requires_from_file(filepath):
    with open(filepath, mode='r') as f:
        for line in iter(f.readline, ''):
            project_name = _line2project_name(line)

            # インストールの除外対象か確認する
            if _is_exclude(project_name):
                continue

            yield line


def _install_requires():
    requires = _load_requires_from_file('requirements.txt')
    return list(requires)


def _test_requires():
    test_requires = _load_requires_from_file('test-requirements.txt')
    return list(test_requires)


def _packages():
    return find_packages(exclude=['*.test', '*.test.*', 'test.*', 'test'])


def main():
    description = 'diagram-autobuild improves the efficiency of the making diagrams.'  # noqa

    setup(
        name='diagram-autobuild',
        version='0.0.1',
        description=description,
        long_description=description,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python',
            'Intended Audience :: Developers',
            'Operating System :: POSIX',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
        ],
        author='momijiame',
        author_email='amedama.ginmokusei@gmail.com',
        url='https://github.com/momijiame/diagram-autobuild',
        zip_safe=False,
        include_package_data=True,
        packages=_packages(),
        install_requires=_install_requires(),
        tests_require=_test_requires(),
        setup_requires=[],
        test_suite='nose.collector',
        entry_points={
            'console_scripts': [
                'diagram-autobuild = diagram_autobuild.cmd.diagram_autobuild_cmd:main',  # noqa
            ],
        }
    )


if __name__ == '__main__':
    main()
