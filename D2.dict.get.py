# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:32:44 2021

@author: TQC
"""

#血型個性資料
dict1={"A":"內向穩重","B":"外向樂觀","O":"堅強自信","AB":"聰明自然"}
blood=input("輸入血型:")
name=dict1.get(blood)
if name==None:
    print("沒有此血型")
else:
    print(name)
