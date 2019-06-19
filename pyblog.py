#!/usr/bin/python3

# Common functions

import datetime

import conf

class Note:
	def __init__(self):
		self.id = -1
		self.title = ""
		self.body = ""
		self.pub_date = datetime.datetime.now()
		self.views = 0

# Don't use it if you've already sent back any data
def err(msg):
	print("Status: 501 {}".format(msg))
	print("Content-Type: text/html")
	print()
	print("Error 501: {}".format(msg))
	exit(0)

# You must send HTTP headers before html data
def send_http_headers():
	print("Content-Type: text/html;charset=UTF-8")
	print()

# Don't use it if you've already sent any data
def http_redirect(url):
	print("Status: 302")
	print("Location: {}".format(url))
	print()
	exit(0)

# Send pyblog header section
def send_header():
	print("<TITLE>{}</TITLE>".format(conf.blog_name))
	print("<LINK rel=\"stylesheet\" type=\"text/css\" href=\"/main.css\">")
	print("<META http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\">")
	print("<H1>{}</H1>".format(conf.blog_name))
