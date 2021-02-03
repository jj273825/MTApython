# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:23:19 2021

@author: TQC
"""

f=open("file1.txt","r")
for line in f:
    print(line)
f.close()

with open("file2.txt","r") as f:
    for line in f:
        print(line)