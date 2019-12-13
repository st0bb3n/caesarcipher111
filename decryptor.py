# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:36:15 2019

@author: Stob
"""

fh = open('encryptor.txt', 'r')
string = list(fh)
key = int(input("key: "))

for line in string[0]:
    if ord(line) == 122:
        letter = (chr(97 - key))
    else:
        nxt = ord(line) - key
        letter = chr(nxt)
    
    print(letter, end = '')

fh.close()