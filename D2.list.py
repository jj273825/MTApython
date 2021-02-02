# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:21:38 2021

@author: TQC
"""

scort=[]
while True: #一直迴圈直到break
    inscort=int(input("分數:"))
    if inscort=="":
        break
    else:
        scort.append(inscort)
        scort2=sorted(scort,reverse=True)
#       scort.sort(
#       scort.reverse()        =scort2
    print(scort2)
