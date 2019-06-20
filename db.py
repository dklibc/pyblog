#!/usr/bin/python3

# just CRUD: get/update/delete objects in DB

import mysql.connector as mariadb

import conf
import pyblog
import auth

conn = mariadb.connect(user=conf.db_user, password=conf.db_pwd,
		       database=conf.db_name)
cursor = conn.cursor()

def get_note(id):
	r = cursor.execute("SELECT id,title,body,pub_date,views FROM note WHERE id=%s", (id,))

#	if r != 1:
#		return None

	res = cursor.fetchone()

	note = pyblog.Note()

	note.id = res[0]
	note.title = res[1]
	note.body = res[2]
	note.pud_date = res[3]
	note.views = res[4]
	return note

def store_note(note):
	if note.id < 0:
		cursor.execute("INSERT INTO note (title,body,pub_date,views) VALUES (%s,%s,%s,%s)",
			       (note.title, note.body, note.pub_date,
			       note.views,))
		note.id = cursor.lastrowid
	else:
		cursor.execute("UPDATE note SET title=%s, body=%s, pub_date=%s, views=%s WHERE id=%s",
			       (note.title, note.body, note.pud_date,
			       note.views, note.id,))
	conn.commit()

def del_note(id):
	cursor.execute("DELETE FROM note WHERE id=%s", (id,))
	conn.commit()

def get_notes(first, count):
	cursor.execute("SELECT id,title,body,pub_date,views FROM note ORDER BY pub_date DESC LIMIT %s, %s", \
		       (first, count,))


	notes = []
	for id, title, body, pub_date, views in cursor:
		note = pyblog.Note()

		note.id = id
		note.title = title

		if body != None:
			i = body.find("[more]", 0)
			if i != -1:
				body = body[:i]

		note.body = body
		note.pub_date = pub_date
		note.views = views

		notes.append(note)

	return notes

def get_notes_count():
	cursor.execute("SELECT COUNT(*) FROM note")
	r = cursor.fetchone()
	return int(r[0])

def get_session():
	cursor.execute("SELECT session_id, session_start from main")

	r = cursor.fetchone()
	if r == None:
		pyblog.err("Failed to read session record from DB")

	session = auth.Session()
	session.id = r[0]
	session.start = r[1]
	return session

def store_session(session):
	cursor.execute("UPDATE main SET session_id=%s, session_start=%s",
		       (session.id, session.start, ))
	conn.commit()
