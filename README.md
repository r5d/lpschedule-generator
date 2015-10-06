# LibrePlanet schedule generator

## dependencies

- nose
- markdown

## on GNU/Linux

Install `virtualenv` and python dev. package.

On a Debian based distribution, do:

    # aptitude install virtualenv python-dev

## set up environment

    $ git clone git://notabug.org/rsd/lpschedule-generator.git

Setup virtual environment:

    $ cd lpschedule-generator
    $ virtualenv .

Activate the virtual environment:

    $ source bin/activate

Install `lpschedule-generator`:

    $ python setup.py install

This will install all the dependencies.
