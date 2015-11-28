import mistune
import re


class HtmlRender(mistune.Renderer):
  """
  Subclassing Renderer classes to customize HTML content.
  
  """
  def header(self, text, level, raw=None):
      if level == 2:
	  return '<header class="program-day-header">\n\t<hgroup>\n\t\t<h%d>%s\n\t\t</h%d>\n\t</hgroup>\n</header>\n' % (level, text+ \
		  '\n\t\t<a class="btn btn-default btn-xs" \n\t\trole="button" '+ \
		  'data-toggle="collapse" \n\t\taria-expanded="false" '+ \
		  'aria-controls="sat-timeslots" '+ \
		  '\n\t\thref="#sat-timeslots">&#x2193;</a>', level)
      elif level == 3:
	  return '\n<article id="sat-ts-b0" class="program-timeslot-break">'+ \
	    '\n\t<header class="program-timeslot-break-header">'+ \
	    '\n\t\t<hgroup>\n\t\t\t<h%d>%s</h%d>\n\t\t</hgroup>\n\t</header>\n</article>\n' % (level, text, level)
	
      return '<h%d>%s</h%d>\n' % (level, text, level)


  def paragraph(self, text):
      _get_room_ptr = re.compile(r'(Room\s[\d]*\-[\d]*)')
      if _get_room_ptr.search(text.strip(' ')) is not None:
	str = _get_room_ptr.findall(text.strip(' '))
	return '<p><span class="label label-default">%s</span></p>\n<a href="#" class="program-session-speaker">%s</a>' \
	  % (''.join(str), _get_room_ptr.sub('',text.strip(' '))) + \
	    '\n<button class="btn btn-default btn-xs" data-toggle="collapse" \n\taria-expanded="false" aria-controls="sat-ts0-s0-collapse"'+ \
	    'data-target="#sat-ts0-s0-collapse">\n\t\tDetails\n</button>\n' 
      else:
	return '<p>%s</p>\n' % text.strip(' ')