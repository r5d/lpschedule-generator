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

import json
import sys

from argparse import ArgumentParser
from collections import OrderedDict
from os import path

from bs4 import BeautifulSoup
from jinja2 import Environment, PackageLoader
from jinja2.exceptions import TemplateNotFound
from mistune import Renderer, Markdown

__version__ = '0.1.0.dev7'

# unicode magic
reload(sys)
sys.setdefaultencoding('utf-8')


# Python dictionary that will contain the lp schedule.
lps_dict = OrderedDict()


def read_file(filename):
    """Read file and return it as a string.

    filename: Absolute pathname of the file.
    """
    content = ''

    try:
        with open(filename, 'rb') as f:
            for line in f:
                content = content + line
    except IOError:
        print "Error: unable to open %s" % filename

    return content


class LPSRenderer(Renderer):
    """Helps in converting Markdown version of LP schedule to a dictionary.
    """
    def __init__(self, **kwargs):
        super(LPSRenderer, self).__init__(**kwargs)
        self.last_day = None
        self.last_time_slot = None
        self.last_session = None

        # Denotes the no. of the paragraph under a session; this
        # information will be helpful in identifying the "speaker",
        # "room" and session "description".
        self.no_paragraph = None


    def header(self, text, level, raw=None):
        global lps_dict

        if level == 2:
            # Add new day.
            lps_dict[text] = OrderedDict()
            self.last_day = text
        elif level == 3:
            # Add new timeslot
            lps_dict[self.last_day][text] = OrderedDict()
            self.last_time_slot = text
        elif level == 4:
            # Add new session
            lps_dict[self.last_day][self.last_time_slot][text] = OrderedDict()
            self.last_session = text
            # We found a new session; set no of paragraphs processed
            # to 0.
            self.no_paragraph = 0

        return super(LPSRenderer, self).header(text, level, raw)


    def paragraph(self, text):
        global lps_dict

        p = super(LPSRenderer, self).paragraph(text)

        if self.no_paragraph == 0:
            # Speaker
            speakers = text.split(', ')

            lps_dict[self.last_day][self.last_time_slot][
                self.last_session]['speakers'] = speakers
            self.no_paragraph = self.no_paragraph + 1
        elif self.no_paragraph == 1:
            # Room
            lps_dict[self.last_day][self.last_time_slot][
                self.last_session]['room'] = text
            # Initialize description
            lps_dict[self.last_day][self.last_time_slot][
                self.last_session]['desc'] = []
            self.no_paragraph = self.no_paragraph + 1
        elif self.no_paragraph > 1:
            lps_dict[self.last_day][self.last_time_slot][
                self.last_session]['desc'].append(text)

        return p


class LPSMarkdown(Markdown):
    """Converts MD LP schedule to a dictionary.

    Returns the Markdown version of LP schedule as a dictionary.
    """
    def __init__(self, inline=None, block=None, **kwargs):
        """
        Initialize with LPSRenderer as the renderer.
        """
        super(LPSMarkdown, self).__init__(renderer=LPSRenderer(),
                                          inline=None, block=None,
                                          **kwargs)


    def parse(self, text):
        global lps_dict

        lps_dict = OrderedDict()
        html = super(LPSMarkdown, self).parse(text)
        return lps_dict


def RenderHTML(lps_dict, year):
    """Renders LP schedule in HTML from a python dictionary.

    Returns the HTML as a string.
    """
    env = Environment(loader=PackageLoader('lpschedule_generator',
                                           'templates'),
                      trim_blocks=True, lstrip_blocks=True)

    template_name = 'lp-sch-%s.jinja2' % year
    template  = None

    try:
        template = env.get_template(template_name)
    except TemplateNotFound as e:
        print "Template %s not found." % template_name
        exit(1)

    lps_html = template.render(schedule=lps_dict)

    return BeautifulSoup(lps_html, 'html.parser').prettify()


def main():
    parser = ArgumentParser()
    parser.add_argument("--version", action="version",
                        version='lpschedule-generator version %s' % __version__,
                        help="Show version number and exit.")
    parser.add_argument("year",
                        help="LP Schedule year.")
    parser.add_argument("lps_md",
                        help="Path to the markdown version of LP Schedule.")
    args = parser.parse_args()

    lps_md_content = read_file(path.abspath(args.lps_md))
    lp_year = args.year

    if lps_md_content:
        markdown = LPSMarkdown()
        lps_dict = markdown(lps_md_content)
        lps_html = RenderHTML(lps_dict, lp_year)
    else:
        exit(1)

    if lps_html:
        # stdout lps html
        print lps_html
    else:
        print 'Error generating LP HTML.'


if __name__ == "__main__":
    main()
