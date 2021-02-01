# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:36:09 2021

@author: TQC
"""

score = int(input("分數:"))
if score>100:
    newscore=int(input("請重新輸入:"))
    if newscore>=90:
        print("A")
    elif newscore>=80:
        print("B")
    elif newscore>=70:
        print("C")
    elif newscore>=60:
        print("D")
    else:
        print("Not Goog")
elif score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("Not Goog")