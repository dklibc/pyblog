#!/usr/bin/python3

# Page with single note
# Get one mandatory param -- 'id'

import cgi
import cgitb

import db
import pyblog

cgitb.enable()

form = cgi.FieldStorage()
id = -1
try:
	id = int(form.getvalue('id'))
except:
	pyblog.err("Missing valid note id")

note = db.get_note(id)
if note == None:
	pyblog.err("No note with this id")

pyblog.send_http_headers()

pyblog.send_header()

print("<P><A href=\"/\">Блог</A>")

print("&nbsp;<A href=\"/pyblog/edit_note.py?id={}\">Редактировать</A>".format(note.id))

print("<H2>{}</H2>".format(note.title))

print("<DIV class=\"note_pub_date\">{}</DIV>".format(note.pud_date.strftime('%d, %b %Y')))

print("<DIV class=\"note_body\">{}</DIV>".format(note.body.replace("[more]", "")))
