#!/usr/bin/python3

# Page with single note
# Get one mandatory param -- 'id'

import cgi
import cgitb

import db
import pyblog
import auth

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

is_auth = auth.is_auth()

pyblog.send_http_headers()

pyblog.send_header()

pyblog.send_top_panel(is_auth, [pyblog.TopPanelLink("/pyblog/edit_note.py?id={}".format(note.id), "Редактировать", True)])

print("<H2>{}</H2>".format(note.title))

print("<DIV class=\"note_pub_date\">{}</DIV>".format(note.pud_date.strftime('%d, %b %Y')))

print("<DIV class=\"note_body\">{}</DIV>".format(note.body.replace("[more]", "")))

pyblog.send_footer()

