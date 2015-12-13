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

from argparse import ArgumentParser
from collections import OrderedDict
from os import path

from mistune import Renderer, Markdown

# Python dictionary that will contain the lp schedule.
lps_dict = OrderedDict()


def read_file(filename):
    """Read file and return it as a string.

    filename: Absolute pathname of the file.
    """
    content = ''

    with open(filename, 'rb') as f:
        for line in f:
            content = content + line

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
            if len(text.split(', ')) == 1:
                speaker_text = text
            else:
                speaker_text = text.split(', ')

            lps_dict[self.last_day][self.last_time_slot][
                self.last_session]['speaker'] = speaker_text
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


def main():
    parser = ArgumentParser()
    parser.add_argument("lps_md",
                        help="Path to the markdown version of LP Schedule.")
    args = parser.parse_args()

    lps_md_content = read_file(path.abspath(args.lps_md))

    markdown = LPSMarkdown()
    lps_dict = markdown(lps_md_content)

    print json.dumps(lps_dict, indent=4)


if __name__ == "__main__":
    main()
