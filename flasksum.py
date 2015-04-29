#/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
sum = Flask(__name__)

@sum.route('/')
def index():
	return 'Welcome to sum page!'

@sum.route('/sum/<int:a>/<int:b>')
def plus(a,b):
	return '%s' % (a + b)

if __name__=='__main__':
	sum.run()
