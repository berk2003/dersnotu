# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 22:34:46 2022

@author: user
"""

list1=["Ali", "Ayşe", "Mustafa", "Merve", "Ela", "Berk"]
list2=["Ali", "Mehmet", "Ayça", "Esin", "Ela", "Merve", "Hasan"]
list3=[]
for x in range (0,len(list2),1):
    if list2[x] in list1:
        list3=list3
    else:
        list3=list3+[list2[x]]