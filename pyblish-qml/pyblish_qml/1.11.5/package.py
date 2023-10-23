# -*- coding: utf-8 -*-

name = 'pyblish_qml'

version = '1.11.5'

description = \
    """
    Frontend for Pyblish written in PyQt5/QML
    """

authors = ['Abstract Factory and Contributors marcus@abstractfactory.com']

requires = ['pyblish_base-1.5.3+']

variants = [['python-3.7']]

def commands():
    env.PYTHONPATH.append('{root}/python')

help = [['Home Page', 'https://github.com/pyblish/pyblish-qml']]

timestamp = 1698044115

hashed_variants = True

pip_name = 'pyblish-qml (1.11.5)'

is_pure_python = True

from_pip = True

format_version = 2
