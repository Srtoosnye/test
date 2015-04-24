#!/usr/bin/env python

f = open('record.txt')
sent = f.readline()
while sent != '':
    print sent,
    sent = f.readline()
f.close()
