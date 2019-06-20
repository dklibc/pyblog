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

class HttpResultCode:
	def __init__(self, code, msg):
		self.code = code
		self.msg = msg

http_res_codes = [ \
	HttpResultCode(400, "Bad Request"), \
	HttpResultCode(401, "Anuthorized"), \
	HttpResultCode(403, "Forbidden"), \
	HttpResultCode(404, "Not Found"), \
	HttpResultCode(500, "Internal Server Error"), \
	HttpResultCode(501, "Not Implemented"), \
];

# Don't use it if you've already sent back any data
def err(msg, errcode = 500):
	s = ""
	for r in http_res_codes:
		if r.code == errcode:
			s = r.msg
			break
	print("Status: {} {}".format(errcode, s))
	print("Content-Type: text/html;charset=ASCII")
	print()
	print("Error {}: {}".format(errcode, msg))
	exit(0)

# Simple reply (signal OK for AJAX?)
def reply_ok(msg, headers = None):
	if headers != None:
		for hdr in headers:
			print(hdr)
	print("Content-Type: text/html;charset=ASCII")
	print()
	print(msg)
	exit(0)

# You must send HTTP headers before html data
def send_http_headers():
	print("Content-Type: text/html;charset=UTF-8")
	print()

# Don't use it if you've already sent any data
#def http_redirect(url):
#	print("Status: 302")
#	print("Location: {}".format(url))
#	print()
#	exit(0)

# Send pyblog header section
def send_header():
	print("<TITLE>{}</TITLE>".format(conf.blog_name))
	print("<LINK rel=\"stylesheet\" type=\"text/css\" href=\"/pyblog/main.css\">")
	print("<META http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\">")
	print("<H1>{}</H1>".format(conf.blog_name))

# Send pyblog footer section
def send_footer():
	print("<DIV class=\"footer\">")
	print("</DIV>")
	print("<SCRIPT type=\"text/javascript\" src=\"/pyblog/main.js\"></SCRIPT>")

class TopPanelLink:
	def __init__(self, href, text, only_auth = False):
		self.href = href
		self.text = text
		self.only_auth = only_auth

def _send_login_form():
		print("<DIV id=\"login_form\">")
		print("&nbsp;&nbsp;<INPUT id=\"login\" size=\"15\"/>")
		print("&nbsp;&nbsp;<INPUT id=\"pwd\" type=\"password\" size=\"15\"/>")
		print("&nbsp;&nbsp;<INPUT type=\"button\" value=\"OK\" onclick=\"pyblog_try_login()\"/>")
		print("&nbsp;&nbsp;<SPAN id=\"login_failed_msg\">Неверный логин или пароль</SPAN>")
		print("</DIV>")

# Send pyblog top panel section
def send_top_panel(is_auth, links = None):
	print("<DIV class=\"top_panel\">")

	print("<A href=\"/\">Блог</A>")

	if links != None:
		for link in links:
			if link.only_auth and is_auth == False:
				continue
			print("&nbsp;&nbsp;<A href=\"{}\">{}</A>".format(link.href, link.text))

	if not is_auth:
		print("&nbsp;&nbsp;<A id=\"login_link\" href=\"\" onclick=\"pyblog_login(); return false;\">Войти</A>")
		_send_login_form()
	else:
		print("&nbsp;&nbsp;<A href=\"\" onclick=\"pyblog_logout(); return false;\">Выйти</A>")

	print("</DIV>")
