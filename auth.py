#!/usr/bin/python3

# Authentication module.
# Params: logout=1, login, pwd.
# We suppose that it will used with AJAX.

import cgi
import cgitb
import time
import datetime
import os
import base64

import db
import pyblog
import conf

class Session:
	def __init__(self):
		self.id = ""
		self.start = datetime.datetime.now()

	def init(self):
		self.id = Session.gen_id()
		self.start = datetime.datetime.now()

	# Generate session id
	@staticmethod
	def gen_id():
#		:22 -- remove "==" padding from the end: base64 converts
#		16 bytes to 22 bytes and padds them to be multiple of 4.
#		.decode(utf-8) -- convert byte array to string
		return base64.b64encode(os.urandom(16))[:22].decode('utf-8')

# Return session id from cookies
def get_ses_id():
	if 'HTTP_COOKIE' not in os.environ:
		return None

	# key1 = value1;key2 = value2;key3 = value3....

	for cookie in map(str.strip, str.split(os.environ['HTTP_COOKIE'], ';')):
		(key, value) = str.split(cookie, '=')
		if key == "pyblog_session":
                        return value

	return None

# Check if user is authenticated
def is_auth():
	# Check session cookie
	id = get_ses_id()
	if id == None:
		return False

	# Validate it
	session = db.get_session()
	if session.id != id or (datetime.datetime.now() - \
	   session.start) / datetime.timedelta(hours=1) > 12:
		return False

	return True

def assert_auth():
	if not is_auth():
		pyblog.err("Forbidden", 403)

# Return session id from cookies
def get_ses_id():
	if 'HTTP_COOKIE' not in os.environ:
		return None

	# key1 = value1;key2 = value2;key3 = value3....

	for cookie in map(str.strip, str.split(os.environ['HTTP_COOKIE'], ';')):
		(key, value) = str.split(cookie, '=')
		if key == "pyblog_session":
                        return value

	return None

# Check if user is authenticated
def is_auth():
	# Check session cookie
	id = get_ses_id()
	if id == None:
		return False

	# Validate it
	session = db.get_session()
	if session.id != id or (datetime.datetime.now() - \
	   session.start) / datetime.timedelta(hours=1) > 12:
		return False

	return True

def assert_auth():
	if not is_auth():
		pyblog.err("Forbidden", 403)


def main():
	cgitb.enable()

	form = cgi.FieldStorage()

	s = form.getvalue('logout')
	if s != None: # Clear session cookie
		cookie = "Set-Cookie: pyblog_session=0; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT"
		pyblog.reply_ok("Logout OK", [cookie])

	# Verify login and password
	s = form.getvalue('login')
	if s == None or s != conf.login:
		pyblog.err("Forbidden", 403)

	s = form.getvalue('pwd')
	if s == None or s != conf.pwd:
		pyblog.err("Forbidden", 403)

	session = Session()
	session.init()
	db.store_session(session)

	# Session is valid 12 hours
	end = time.gmtime(time.time() + 12*60*60)
	expires = time.strftime("%a, %d-%b-%Y %T GMT", end)
	cookie = "Set-Cookie: pyblog_session={}; Expires={}; Path=/;".format(session.id, expires)

	pyblog.reply_ok("Login ok", [cookie])


if __name__ == '__main__':
	main()
