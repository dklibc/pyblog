#!/usr/bin/python3

# Page where you can edit note.
# Get one optional param -- 'id' (it is mising for new notes).

import cgi
import cgitb

import pyblog
import db
import markup

cgitb.enable()

form = cgi.FieldStorage()

s = form.getvalue('id')
if s != None:
	id = -1;
	try:
		id = int(s)
	except:
		pyblog.err("Invalid note id")

	note = db.get_note(id)
	if note == None:
		pyblog.err("No note with this id")
else:
	note = pyblog.Note()

pyblog.send_http_headers()

pyblog.send_header()

print("<P><A href=\"/\">Блог</A>")

print("<H2>Редактировать запись</H2>")

print("<FORM action=\"/pyblog/store_note.py\" method=\"post\">")

if note.id >= 0:
	print("<INPUT name=\"id\" type=\"hidden\" value=\"{}\">".format(note.id))

print("<P><INPUT name=\"title\" maxlength=\"255\" size=\"40\" value=\"{}\">".format(note.title))

print("<P><TEXTAREA name=\"body\" rows=\"30\" cols=\"80\" style=\"padding: 1em;\">{}</TEXTAREA>".format(markup.html2wiki(note.body)))

if note.id >= 0:
	s = "Готово"
else:
	s = "Запостить"

print("<P><INPUT type=\"submit\" value=\"{}\">".format(s))

print("</FORM>")
