# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


version = '0.1'
description = 'Collection of `mr.bob` plone templates.'
long_description = open('README.rst').read() + open('HISTORY.rst').read() + \
    open('LICENSE').read()

setup(
    name='bobtemplates.plone',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Gil Forcada',
    author_email='gforcada@gnome.org',
    url='https://github.com/gforcada/bobtemplates.plone',
    license='LGPL',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    namespace_packages=['bobtemplates'],
    install_requires=[
        'setuptools',
        'mr.bob',
    ],
    entry_points="""
    """,
)
