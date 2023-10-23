# -*- coding: utf-8 -*-

name = 'pyblish_lite'

version = '0.8.12'

description = \
    """
    Lightweight graphical user interface to Pyblish
    """

authors = ['Abstract Factory and Contributors marcus@abstractfactory.com']

requires = ['pyblish_base-1.4+']

variants = [['python-3.7']]

def commands():
    env.PYTHONPATH.append('{root}/python')

help = [['Home Page', 'https://github.com/pyblish/pyblish-lite']]

timestamp = 1698047491

hashed_variants = True

from_pip = True

is_pure_python = True

pip_name = 'pyblish-lite (0.8.12)'

format_version = 2
