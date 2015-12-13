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

import mistune

class Mark2html(object):
  """
  Converts Markdown to HTML format. `mistune` parser is used.
  
  Attributes:
      FileName : Markdown File descriptor
  """
  def __init__(self, FileName):
    """ 
    Returns a Mark2html object 
    """
    self.FileName = FileName
    
  def PrintHTML(self):
    """
    Prints HTML format of FileName
    """
    print mistune.markdown(self.FileName.read())
    
  def GetHTML(self):
    """
    Returns HTML format of FileName
    """
    return mistune.markdown(self.FileName.read())
