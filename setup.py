#!/usr/bin python3

"""
Coronavirus (COVID-19) Dashboard - API Service
==============================================

Software Development Kit (SDK)
------------------------------

This is a Python SDK for the COVID-19 API, as published by
Public Health England on `Coronavirus (COVID-19) in the UK`_
dashboard.

The endpoint for the data provided using this SDK is:

    https://api.coronavirus.data.gov.uk/v1/data

.. _`Coronavirus (COVID-19) in the UK`: http://coronavirus.data.gov.uk/


License: MIT

Copyright (c) 2020, Public Health England
"""

from setuptools import setup
from os.path import join, dirname, abspath


package_dir = dirname(abspath(__file__))


def get_meta():
    from importlib.util import spec_from_file_location, module_from_spec

    keys = {
        '__description__',
        '__copyright__',
        '__license__',
        '__url__',
        '__version__'
    }

    path = join(package_dir, 'uk_covid19', '__init__.py')

    spec = spec_from_file_location('.', path)
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)

    meta = {key.replace('__', ''): getattr(mod, key) for key in keys}

    return meta


def get_requirements():
    with open(join(package_dir, 'requirements.txt')) as requirements:
        req = requirements.read().splitlines()
    return req


def readme():
    with open(join(package_dir, 'README.rst')) as f:
        return f.read()


metadata = get_meta()


setup(
    name='uk_covid19',
    version=metadata.get('version'),
    packages=['uk_covid19'],
    url=metadata.get('url'),
    license=metadata.get('license'),
    author='Pouria Hadjibagheri',
    author_email='Pouria.Hadjibagheri@phe.gov.uk',
    maintainer='Public Health England - Coronavirus Dashboard Team',
    maintainer_email='covid19-tech@phe.gov.uk',
    description=metadata.get('description'),
    include_package_data=True,
    long_description=readme(),
    long_description_content_type='text/x-rst',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development',
        'Topic :: Database',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords=(
        'API SDK PHE COVID19 COVID-19 coronavirus data '
        'UK England Wales Scotland Northern_Ireland United_Kingdom'
    ),
    install_requires=get_requirements(),
    python_requires='>=3.7',
    tests_require=["pytest"],
    test_suite='tests'
)
