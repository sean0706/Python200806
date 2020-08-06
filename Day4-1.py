# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:23:47 2020

@author: user
"""

import os.path

if os.path.isfile('myfile.txt'):
    print('file存在')
else:
    print('file不存在')
    
h=open('myfile.txt','w')
h.write('hi hi hi!!!')

h=open('myfile.txt','r')
s=h.read()
print(s)

h=open('myfile.txt','a')
h.write('hello hello hello!!!')

h.close()


