#!/usr/bin/python3

# Update/create note in DB.
# Optional params: id, title, body.

import cgi
import cgitb

import db
import pyblog
import markup

cgitb.enable()

form = cgi.FieldStorage()

id = -1

s = form.getvalue('id')
if s != None:
	try:
		id = int(s)
	except:
		pyblog.err("Invalid note id")

if id < 0:
	note = pyblog.Note()
else:
	note = db.get_note(id)
	if note == None:
		pyblog_err("No note with this id")

s = form.getvalue('title')
if s != None:
	note.title = s

s = form.getvalue('body')
if s != None:
	note.body = markup.wiki2html(s)

db.store_note(note)

pyblog.http_redirect("/")
