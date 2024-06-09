#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo-confd-whitelist',
    version='0.1',
    description='Workano whitelist plugin',
    author='Mohsen Rezvani',
    author_email='foo@bar.com',
    packages=find_packages(),
    url='https://www.foo-bar.com',
    include_package_data=True,
    package_data={
        'wazo_confd_whitelist': ['api.yml'],
    },
    entry_points={
        'wazo_confd.plugins': [
            'whitelist = wazo_confd_whitelist.plugin:Plugin'
        ]
    },
    install_requires=[
        # List your dependencies here
    ],
)
