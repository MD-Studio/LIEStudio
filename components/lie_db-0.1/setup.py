#! /usr/bin/env python
# -*- coding: utf-8 -*-

# package: lie_db
# file: setup.py
#
# Part of ‘lie_db’, a package providing MongoDB access for the LIEStudio
# package.
#
# Copyright © 2016 Marc van Dijk, VU University Amsterdam, the Netherlands
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

distribution_name = 'lie_db'
main_module = __import__(distribution_name)
main_module_doc = main_module.__doc__

setup(
    name=distribution_name,
    version=main_module.__version__,
    description='PyMongo database drivers for the LIEStudio application',
    author='Marc van Dijk, VU University, Amsterdam, The Netherlands',
    author_email='m4.van.dijk@vu.nl',
    url=main_module.__url__,
    license=main_module.__licence__,
    keywords='MongoDB PyMongo LIEStudio database',
    long_description=main_module_doc,
    platforms=['Any'],
    packages=find_packages(),
    py_modules=[distribution_name],
    install_requires=['pymongo'],
    test_suite="tests",
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'autobahn.twisted.wamplet': [
            'wamp_services = lie_db.wamp_services:make'
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Database',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        ],
)