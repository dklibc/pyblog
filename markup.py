#!/usr/bin/python3

# Functions for convertion of wiki markup to html and vice versa.

def html2wiki(s):
	s = s.replace("&lt;", "<")
	s = s.replace("&gt;", ">")
	s = s.replace("&amp;", "&")
	s = s.replace("<P>", "\r\n")
	return s

def wiki2html(s):
	s = s.replace("&", "&amp;")
	s = s.replace("<", "&lt;")
	s = s.replace(">", "&gt;")
	s = "<P>" + s
	s = s.replace("\r\n\r\n", "\r\n<P>")
	return s
