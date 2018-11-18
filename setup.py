#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='simple_redis_queue',
    version='1.0',
    description='Simple Queue',
    long_description=open('README.md').read(),
    author='aamishbaloch',
    url='https://github.com/aamishbaloch/simple_redis_queue',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'redis>=3.0',
    ],
)
