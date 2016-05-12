Installation
------------

On a Debian based distribution, do::

  # aptitude install virtualenv python-setuptools

Install globally
~~~~~~~~~~~~~~~~

::

   $ sudo pip install lpschedule-generator


Install locally using virtualenv (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make a separate ``lpschedule-generator`` directory and initialize the
virtual environment in it::

  $ mkdir lpschedule-generator
  $ cd lpschedule-generator

  $ virtualenv .
  $ source bin/activate

Install ``lpschedule-generator`` inside this directory using ``pip``::

  $ pip install lpschedule-generator

Activating virtual environment
``````````````````````````````

Always activate the virtual environment before using the ``lps_gen``
command::

   $ cd path/to/lpschedule-generator
   $ source bin/activate
