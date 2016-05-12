LP speakers
-----------

LP speakers usage
~~~~~~~~~~~~~~~~~
::

   $ lps_gen -sp path/to/lp-speakers.jinja2 path/to/lp-speakers.md > path/to/speakers-content.html

or::

  $ lps_gen --speakers path/to/lp-speakers.jinja2 path/to/lp-speakers.md > path/to/speakers-content.html

LP speakers markdown structure
``````````````````````````````

::

   # Keynote speaker name 1

   ![Keynote speaker name 1 - Photo](//fsf.org/images/ks1.jpg)

   Lorem ipsum dolor sit amet keynote speaker 1 bio; can contain
   inline HTML.

   # Keynote speaker name 2

   ![Keynote speaker name 2 - Photo](//fsf.org/images/ks2.jpg)

   Lorem ipsum dolor sit amet keynote speaker 2 bio; can contain
   inline HTML.

   ...

   ## Speaker name 1

   ![Speaker name 1 - Photo](//fsf.org/images/s1.jpg)

   Lorem ipsum dolor sit amet speaker 1 bio; can contain inline HTML.

   ## Speaker name 2

   ![Speaker name 2 - Photo](//fsf.org/images/s2.jpg)

   Lorem ipsum dolor sit amet speaker 2 bio; can contain inline HTML.

   ...


Everything except the speaker name is optional.

Sample: https://notabug.org/rsd/lpschedule-generator/raw/dev/tests/files/lp-speakers.md

Speaker's ID generation
+++++++++++++++++++++++

The last name of the speaker is automatically made the ID; if a
speaker' name is "John Hacker", the ID for this speaker will be
``hacker``.

- If two or more speakers have the same last name, then, the first
  speaker will have their last name as their ID and from the second to
  the n^th speaker will have their full name as their ID; if "Bill
  Hacker" and "Jill Hacker" are two speakers, "Bill" will get
  ``hacker`` as his ID and "Jill" will get ``jill_hacker`` as her ID.

- The IDs are transliterated to ASCII; if a speaker' name is "John
  HÖcker", the ID for this speaker will be ``hacker``.
