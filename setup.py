#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo-confd-whitelist',
    version='0.1',
    description='Workano whitelist plugin',
    author='Mohsen Rezvani',
    author_email='mohsenrzva@gmail.com',
    packages=find_packages(),
    url='',
    include_package_data=True,
    package_data={
        'wazo_confd_whitelist': ['api.yml'],
    },
    entry_points={
        'wazo_confd.plugins': [
            'whitelist = wazo_confd_whitelist.plugin:Plugin'
        ]
    },
)
