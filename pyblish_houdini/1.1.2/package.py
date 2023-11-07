# -*- coding: utf-8 -*-

name = 'pyblish_houdini'

version = '1.1.2'

description = 'Houdini Pyblish package'

authors = ['Abstract Factory and Contributors marcus@abstractfactory.io']

requires = ['pyblish_base-1.4+']

variants = [['python-3.7']]

def commands():
    env.PYTHONPATH.append('{root}/python')

help = [['Home Page', 'https://github.com/pyblish/pyblish-houdini']]

timestamp = 1699344811

hashed_variants = True

is_pure_python = True

from_pip = True

pip_name = 'pyblish-houdini (1.1.2)'

format_version = 2
