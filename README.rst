LibrePlanet schedule generator
==============================

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


Usage
-----

::

   $ lps_gen YEAR path/to/lp-sch.md > path/to/program-schedule.html

Replace ``YEAR`` with LP year; for example, for generating LP 2016
schedule, the command will be::

  $ lps_gen 2016 path/to/lp-sch.md > path/to/program-schedule.html


LP schedule markdown structure
------------------------------

Overall structure::

   ## Day 1

   ### Timeslot 1

   #### Session 1

   #### Session 2

   ...

   ### Timeslot 2

   #### Session 1

   #### Session 2

   ...

   ## Day 2

   ### Timeslot 1

   #### Session 1

   #### Session 2

   ...


Session structure::

  #### Fork and ignore: fighting a GPL violation by coding instead

  [Bradley Kuhn][kuhn], [Karen Sandler][sandler]

  Room 32-155

  Typically, GPL enforcement activity involves copyright infringement
  actions which compel license violators to correct errors in their
  GPL compliance, defending the policy goals of the GPL: the rights of
  developers and users to copy, share, modify and redistribute.

  While traditional enforcement is often undeniably necessary for
  embedded electronics products, novel approaches to GPL violations
  are often possible and even superior for more traditional software
  distributions.

  Recently, [Software Freedom Conservancy][sfc] engaged in an
  enforcement action whereby, rather than fight the violator in court,
  we instead provided resources and assistance to a vetted
  GPL-compliant fork of a violating codebase.

  This talk discusses which scenarios make this remedy optimal and the
  lessons learned. The talk includes some licensing and technical
  content about vetting the licensing information of codebases.

  [kuhn]: https://libreplanet.org/YEAR/path/to/speakers.html#kuhn
  [sandler]: https://libreplanet.org/YEAR/path/to/speakers.html#sandler
  [sfc]: https://sfconservancy.org/


Sample: https://notabug.org/rsd/lpschedule-generator/raw/dev/tests/files/lp-sch.md


Source
------

::

   $ git clone https://notabug.org/rsd/lpschedule-generator.git
