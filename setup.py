#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo-confd-mohsen',
    version='0.1',
    description='Workano mohsen plugin',
    author='Mohsen Rezvani',
    author_email='foo@bar.com',
    packages=find_packages(),
    url='https://www.foo-bar.com',
    include_package_data=True,
    package_data={
        'wazo_confd_mohsen': ['api.yml'],
    },
    entry_points={
        'wazo_confd.plugins': [
            'mohsen = wazo_confd_mohsen.plugin:Plugin'
        ]
    },
    install_requires=[
        # List your dependencies here
    ],
)
