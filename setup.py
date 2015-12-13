#    Copyright (C) 2015  lpschedule-generator author(s). See AUTHORS.
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

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'LibrePlanet schedule generator',
    'author': 'rsiddharth',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'rsd@gnu.org',
    'version': '0.0',
    'install_requires': ['nose', 'mistune'],
    'packages': ['lpschedule'],
    'scripts': [],
    'name': 'lpschedule-generator'
    }

setup(**config)
