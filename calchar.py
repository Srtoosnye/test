#!/usr/bin/env python

s = raw_input('Please input text: ')
cal = []
for i in range(0,26):
    cal.append(0)
for i in range(0,len(s)):
    if s[i]=='a':
        cal[0] = cal[0] + 1
    if s[i]=='b':
        cal[1] = cal[1] + 1
    if s[i]=='c':
        cal[2] = cal[2] + 1
    if s[i]=='d':
        cal[3] = cal[3] + 1
    if s[i]=='e':
        cal[4] = cal[4] + 1
    if s[i]=='f':
        cal[5] = cal[5] + 1
    if s[i]=='g':
        cal[6] = cal[6] + 1
    if s[i]=='h':
        cal[7] = cal[7] + 1
    if s[i]=='i':
        cal[8] = cal[8] + 1
    if s[i]=='j':
        cal[9] = cal[9] + 1
    if s[i]=='k':
        cal[10] = cal[10] + 1
    if s[i]=='l':
        cal[11] = cal[11] + 1
    if s[i]=='m':
        cal[12] = cal[12] + 1
    if s[i]=='n':
        cal[13] = cal[13] + 1
    if s[i]=='o':
        cal[14] = cal[14] + 1
    if s[i]=='p':
        cal[15] = cal[15] + 1
    if s[i]=='q':
        cal[16] = cal[16] + 1
    if s[i]=='r':
        cal[17] = cal[17] + 1
    if s[i]=='s':
        cal[18] = cal[18] + 1
    if s[i]=='t':
        cal[19] = cal[19] + 1
    if s[i]=='u':
        cal[20] = cal[20] + 1
    if s[i]=='v':
        cal[21] = cal[21] + 1
    if s[i]=='w':
        cal[22] = cal[22] + 1
    if s[i]=='x':
        cal[23] = cal[23] + 1
    if s[i]=='y':
        cal[24] = cal[24] + 1
    if s[i]=='z':
        cal[25] = cal[25] + 1
for i in range(0,26):
    if cal[i] != 0:
        print chr(i+97),':',cal[i]
