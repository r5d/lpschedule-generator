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
    'install_requires': ['nose'],
    'packages': ['lpschedule'],
    'scripts': [],
    'name': 'lpschedule-generator'
    }

setup(**config)
