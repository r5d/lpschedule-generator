.. highlight:: shell

Installation
------------

On a Debian based distribution, do::

  $ sudo apt-get install python-pip

On GNU Guix, do::

  $ guix package -i python-pip


Install globally
~~~~~~~~~~~~~~~~

::

   $ sudo pip install lpschedule-generator


Install locally using virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First get ``virtualenv``.

On a Debian based distribution, do::

  $ sudo apt-get install virtualenv

On GNU Guix, do::

  $ guix package -i python-virtualenv

Make a separate ``lpschedule-generator`` directory and initialize the
virtual environment in it::

  $ mkdir lpschedule-generator
  $ cd lpschedule-generator

  $ virtualenv -p python2.7 .
  $ source bin/activate

Install ``lpschedule-generator`` inside this directory using ``pip``::

  $ pip install lpschedule-generator

Activating virtual environment
``````````````````````````````

Always activate the virtual environment before using the ``lps_gen``
command::

   $ cd path/to/lpschedule-generator
   $ source bin/activate


Test
~~~~

Do::

  $ lps_gen --help

.. highlight:: text

You must get::

  usage: lps_gen [-h] [-s | -sp] [--ical ICAL] [--version] lp_t lp_md

  positional arguments:
    lp_t             Path to the LP template.
    lp_md            Path to the LP markdown.

  optional arguments:
    -h, --help       show this help message and exit
    -s, --schedule   Generate LP schedule
    -sp, --speakers  Generate LP speakers
    --ical ICAL      Specify LP year as argument; generates iCal
    --version        Show version number and exit.

If the ``lps_gen`` command is installed, move to the :ref:`next
section <lps-doc-sec-schedule>`; otherwise ask for
:ref:`lps-doc-sec-help`.
