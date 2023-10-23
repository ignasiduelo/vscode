# -*- coding: utf-8 -*-

name = 'pyblish_base'

version = '1.8.11'

description = \
    """
    Plug-in driven automation framework for content
    """

authors = ['Abstract Factory and Contributors marcus@abstractfactory.io']

tools = ['pyblish']

variants = [['platform-osx', 'arch-x86_64', 'python-3.7']]

def commands():
    env.PYTHONPATH.append('{root}/python')
    env.PATH.append('{root}/bin')

help = [['Home Page', 'https://github.com/pyblish/pyblish']]

timestamp = 1698044115

hashed_variants = True

pip_name = 'pyblish-base (1.8.11)'

is_pure_python = True

from_pip = True

format_version = 2
