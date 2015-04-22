#!/usr/bin/env python

n = int(raw_input("Please input a number: "))
if n==0 or n==1:
    print "No!"
    exit()
a = range(2,n+1)
for i in a:
    f = 1
    b = range(2,i/2+1)
    for j in b:
        if i % j == 0:
            f = 0
            break
    if f == 1:
        print i,
