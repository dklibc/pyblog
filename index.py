#!/usr/bin/python3

# pyblog main page: notes ordered by publication data, last first
# Get one optional param 'page' (default=1)

import cgi
import cgitb
import sys
import locale

# Here python will search for our modules
sys.path.append("./pyblog")

import conf
import db
import pyblog
import auth

def note_preview(note):
	print("<DIV class=\"note_preview\">");
	print("<DIV class=\"note_preview_title\">")
	print(note.title)
	print("</DIV>")
	print("<DIV class=\"note_preview_date\">")
	print(note.pub_date.strftime('%d, %b %Y'))
	print("</DIV>")
	print("<DIV class=\"note_preview_body\">")

	if note.body != None:
		i = note.body.find("[more]", 0)
		if i != -1:
			print(note.body[:i])
		else:
			print(note.body)

	print("</DIV>")
	print("<DIV><A href=\"/pyblog/note.py?id={}\">Читать дальше</A></DIV>".format(note.id))
	print("</DIV>")

def print_nav_panel(cur_page, last_page):
	nav_html = "<A href=\"/?page={}\">{}</A>&nbsp;"
	nav_html_cur = "<A class=\"notes_nav_cur\" href=\"/?page={}\">{}</A>&nbsp;"

	print("<DIV class=\"notes_nav\">")

	if cur_page > 1:
		print(nav_html.format(cur_page - 1, "&lt;"))

	i = 1
	while i <= last_page:
		if i == cur_page:
			print(nav_html_cur.format(i, i))
		else:
			print(nav_html.format(i, i))
		i += 1

	if cur_page < last_page:
		print(nav_html.format(cur_page + 1, "&gt;"))

	print("</DIV>")

cgitb.enable()

form = cgi.FieldStorage()

page_num = 1
s = form.getvalue('page')
if s != None:
	try:
		page_num = int(s, 10)
	except:
		page_num = 1

notes_count = db.get_notes_count()

last_page = (notes_count + conf.notes_on_page - 1) // conf.notes_on_page

if page_num > last_page and notes_count != 0:
	page_num = last_page

offset = (page_num - 1) * conf.notes_on_page

notes = db.get_notes(offset, conf.notes_on_page)

is_auth = auth.is_auth()

pyblog.send_http_headers()

pyblog.send_header()

pyblog.send_top_panel(is_auth, [ pyblog.TopPanelLink("/pyblog/edit_note.py", "Новая запись", True) ])

# For rus month abbrev in date
locale.setlocale(locale.LC_ALL, "ru_RU.utf8")

for note in notes:
	note_preview(note)

print_nav_panel(page_num, last_page)

pyblog.send_footer()
