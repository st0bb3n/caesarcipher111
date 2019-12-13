# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:53:28 2019

@author: Stob
"""

fh = open('encryptor.txt', 'w')

string = str(input("Message: "))
string = string.lower()
key = int(input("key: "))


for i in string:
    if ord(i) == 122:
        letter = (chr(97 + key))
    else:
        nxt = ord(i) + key
        letter = chr(nxt)
        
    fh.write(letter)

fh.close()
