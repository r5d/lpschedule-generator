.. _lps-doc-sec-schedule:

LP schedule
-----------

.. highlight:: text

Markdown structure
~~~~~~~~~~~~~~~~~~

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

Level two heading (``##``) format::

  ## Saturday, March 19

  ...

  ## Sunday, March 20

Level three heading (``###``) format::

  ### 09:00 - 09:45: Registration and Breakfast

  ### 09:45 - 10:45: Opening Keynote

  ...

  ### 10:55 - 11:40: Session Block 1A

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


Auto-linking speaker names
++++++++++++++++++++++++++

Speakers in the schedule MD can be auto-linked to speakers' page by
marking them up like this ``[John Hacker]()``

The script converts:

- ``[John Hacker]()`` to ``<a href="speakers.html#hacker">John
  Hacker</a>`` if John Hacker's bio is available in the speakers' page.

- ``[John Hacker]()`` to ``John Hacker`` if John Hacker's bio is not
  available in the speakers' page. In this case, the script also appends
  ``John Hacker`` name in the ``speakers.noids`` file.

  The ``speakers.noids`` file contains a list of speakers who were
  auto-linked in the schedule MD but who's bio is not (yet) available
  in the speakers' page.

For auto-linking speakers, the script uses the ``speakers.ids`` file;
this file is written to the disk after generating the the speakers'
page from MD. Generate the speakers' page before generating the
schedule page for auto-linking to work.

Sample: https://notabug.org/rsd/lpschedule-generator/raw/dev/tests/files/lp-sessions-autolink.md

Special cases
+++++++++++++

Speaker TBA
...........

When the speaker information for a session is not yet available put
``SpeakerTBA`` as the placeholder in the line that usually contains
the speaker information; the rendered HTML will not have speaker
information for sessions that have ``SpeakerTBA``.

Room TBA
........

When a room for a session is not yet available put ``RoomTBA`` as the
placeholder in the line that usually contains the room number; the
rendered HTML will not have the room number for sessions that have
``RoomTBA``.

Description TBA
...............

When the description for session is not yet available put ``DescTBA``
as the placeholder; the rendered HTML will not have the description
for sessions that have ``DescTBA``.

Sample: https://notabug.org/rsd/lpschedule-generator/raw/dev/tests/files/lp-sch-tba.md

Sessions only schedule
......................

It is possible to have a sessions only schedule. To do this, at the
beginning of the markdown document:

- Add a level two heading (``##``) with one or more whitespaces.
- Add a level three heading (``###``) with one or more whitespaces.

Sessions only sample: https://notabug.org/rsd/lpschedule-generator/raw/dev/tests/files/lp-sch-sessions-only.md

Single session time slot
........................

If a time slot contains only one session (like a Keynote), then
session heading/title can be omitted::

  ### 9:00 - 10:45: Opening Keynote - Beyond unfree...

  [Cory Doctorow][doctorow]

  Room 32-123

  Software has eaten the world...

.. highlight:: bash

Generate HTML from Markdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

   $ lps_gen -s path/to/lp-sch.jinja2 path/to/lp-sch.md > path/to/program-schedule.html

or::

  $ lps_gen --schedule path/to/lp-schedule.jinja2 path/to/lp-sch.md > path/to/program-schedule.html


iCal export
~~~~~~~~~~~

The ``--ical`` switch enables iCal export while generating LP
schedule::

  $ lps_gen -s --ical 2016 path/to/lp-schedule.jinja2 path/to/lp-schedule.md > path/to/program-schedule.html

The year of the conference must be given as an argument to the
``--ical`` switch.

If you run into issues, ask for :ref:`help <lps-doc-sec-help>`.

Next, you might want to look at the :ref:`lps-doc-sec-speakers` section or the :ref:`lps-doc-sec-general` section.
