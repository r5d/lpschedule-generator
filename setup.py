#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2015  lpschedule-generator contributors. See CONTRIBUTORS.
#
#    This file is part of lpschedule-generator.
#
#   lpschedule-generator is free software: you can redistribute it
#   and/or modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation, either version 3 of
#   the License, or (at your option) any later version.
#
#   lpschedule-generator is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with lpschedule-generator (see COPYING).  If not, see
#   <http://www.gnu.org/licenses/>.

import lps_gen

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'lpschedule-generator',
    'description': 'LibrePlanet schedule generator',
    'long_description': lps_gen.read_file('README.md'),
    'version': lps_gen.__version__,
    'platforms': 'GNU/Linux',
    'license': 'GNU General Public License version 3 or later',
    'url': 'https://notabug.org/rsd/lpschedule-generator/',
    'author': 'rsiddharth',
    'author_email': 'rsd@gnu.org',
    'install_requires': ['nose', 'mock', 'mistune', 'Jinja2', 'beautifulsoup4'],
    'py_modules': ['lps_gen'],
    'data_files':[('templates',['templates/lp-sch-2016.jinja2'])],
    'entry_points': {
        'console_scripts': ['lps_gen = lps_gen:main']
    },
}

setup(**config)
