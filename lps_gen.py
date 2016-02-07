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
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound
from mistune import Renderer, Markdown
from unidecode import unidecode

__version__ = '0.1.1'

# unicode magic
reload(sys)
sys.setdefaultencoding('utf-8')


# Python dictionary that will contain the lp schedule.
lps_dict = OrderedDict()

# Python dictionary that will contain the lp speakers.
lpspeakers_dict = OrderedDict()

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


class LPSpeakersRenderer(Renderer):
    """Helps in converting Markdown version of LP speakers to a dictionary.
    """

    def __init__(self, **kwargs):
        super(LPSpeakersRenderer, self).__init__(**kwargs)
        global lpspeakers_dict

        lpspeakers_dict = OrderedDict()
        lpspeakers_dict['keynote-speakers'] = []
        lpspeakers_dict['speakers'] = []

        # Type of present speaker being processed; can either be
        # 'keynote-speakers' or 'speakers'.'
        self.speaker_type = None

        # Maintain a list of used IDs
        self.used_ids = []


    def mk_uid(self, text):
        """Returns a unique id.
        """
        # 'John HÖcker, Onion Project' -> 'John HÖcker'
        text = text.split(', ')[0]

        # 'John HÖcker' -> 'John Hacker'
        ascii_text = unidecode(unicode(text))

        # 'John Hacker' -> 'hacker'
        id_ = ascii_text.split()[-1].lower()

        if id_ not in self.used_ids:
            self.used_ids.append(id_)
            return id_
        else:
            # 'John Hacker' -> 'john_hacker'
            id_ = '_'.join([s.lower() for s in ascii_text.split()])
            self.used_ids.append(id_)
            return id_


    def header(self, text, level, raw=None):
        global lpspeakers_dict

        if level == 1:
            self.speaker_type = 'keynote-speakers'
            lpspeakers_dict[self.speaker_type].append(OrderedDict())

            lpspeakers_dict[self.speaker_type][-1]['speaker'] = text
            lpspeakers_dict[self.speaker_type][-1]['id'] = self.mk_uid(text)
            lpspeakers_dict[self.speaker_type][-1]['bio']  = []
        elif level == 2:
            self.speaker_type = 'speakers'
            lpspeakers_dict[self.speaker_type].append(OrderedDict())

            lpspeakers_dict[self.speaker_type][-1]['speaker'] = text.split(', ')[0]
            lpspeakers_dict[self.speaker_type][-1]['id'] = self.mk_uid(text)
            lpspeakers_dict[self.speaker_type][-1]['bio']  = []

        return super(LPSpeakersRenderer, self).header(text, level, raw)


    def image(self, src, title, text):
        global lpspeakers_dict

        lpspeakers_dict[self.speaker_type][-1]['img_url'] = src
        lpspeakers_dict[self.speaker_type][-1]['img_alt'] = text

        return super(LPSpeakersRenderer, self).image(src, title, text)


    def paragraph(self, text):
        global lpspeakers_dict

        p = super(LPSpeakersRenderer, self).paragraph(text)

        if text.startswith('<img'):
            # ignore
            return p

        lpspeakers_dict[self.speaker_type][-1]['bio'].append(text)
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


class LPSpeakersMarkdown(Markdown):
    """Converts MD LP speakers to a dictionary.

    Returns the Markdown version of LP speakers as a dictionary.
    """

    def __init__(self, inline=None, block=None, **kwargs):
        """
        Initialize with LPSpeakersRenderer as the renderer.
        """
        super(LPSpeakersMarkdown, self).__init__(renderer=LPSpeakersRenderer(),
                                                 inline=None, block=None,
                                                 **kwargs)


    def parse(self, text):
        global lpspeakers_dict

        html = super(LPSpeakersMarkdown, self).parse(text)
        return lpspeakers_dict


def RenderHTML(lp_dict, template):
    """Renders LP schedule/speakers in HTML from a python dictionary.

    Returns the HTML as a string.
    """
    env = Environment(loader=FileSystemLoader(path.dirname(template)),
                      trim_blocks=True, lstrip_blocks=True)

    template_name = path.basename(template)
    template  = None

    try:
        template = env.get_template(template_name)
    except TemplateNotFound as e:
        print "Template %s not found." % template_name
        exit(1)

    lp_html = template.render(lp_dict=lp_dict)

    return BeautifulSoup(lp_html, 'html.parser').prettify()


def main():
    parser = ArgumentParser()
    parser.add_argument("--version", action="version",
                        version='lpschedule-generator version %s' % __version__,
                        help="Show version number and exit.")
    parser.add_argument("lp_t",
                        help="Path to the LP template.")
    parser.add_argument("lp_md",
                        help="Path to the LP markdown.")
    args = parser.parse_args()

    lp_template = args.lp_t
    lp_md_content = read_file(path.abspath(args.lp_md))

    if path.exists(lp_template) and lp_md_content:
        markdown = LPSMarkdown()
        lp_dict = markdown(lp_md_content)
        lp_html = RenderHTML(lp_dict, lp_template)
    else:
        exit(1)

    if lp_html:
        # stdout lps html
        print lp_html
    else:
        print 'Error generating LP HTML.'


if __name__ == "__main__":
    main()
