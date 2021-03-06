#!/usr/bin/env python3
import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='',
    version='0.1',
    author='Alex Ellwein',
    author_email='alex.ellwein@gmail.com',
    url='',
    description='',
    packages=find_packages(),
    long_description=read('README.md'),
    license=read('LICENSE.md'),
    install_requires=[],
    entry_points={
        'console_scripts': []
    }
)
