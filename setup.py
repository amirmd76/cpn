# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cpn',
    version='1.0.0',
    description='Python client for using Charzeh Pull Notification system on server-side',
    long_description=readme,
    author='AmirMohammad Dehghan',
    author_email='amirmd76@gmail.com',
    url='https://github.com/amirmd76/cpn.git',
    license=license,
    packages=find_packages()
)
