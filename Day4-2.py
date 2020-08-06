# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:59:02 2020

@author: user
"""
t=0
file=open("cat.jpg","rb")
img=file.read()
file.close()


while t<10:
    file=open('複製.jpg','wb')
    file.write(img)
    t=+1
    file.close()