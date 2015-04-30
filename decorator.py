#!/usr/bin/env python

def route(suffix):
	def decorator(f):
		def wrapped():
			return f() + suffix
		return wrapped
	return decorator

s = raw_input()
@route(s)
def index():
	return '127.0.0.1:5000/'

print index()
