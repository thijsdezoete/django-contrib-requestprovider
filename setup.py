#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(name='gadjo',
    version=".".join(map(str, __import__("coffin").__version__)),
    description='Request provider for Django',
    author='dontknow',
    author_email='thijsdezoete@gmail.com',
    maintainer='not me',
    maintainer_email='someoneelse@gmail.com',
    url='https://github.com/thijsdezoete/django-contrib-requestprovider',
    packages=find_packages(),
    #install_requires=['Jinja2', 'django>=1.2'],
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
