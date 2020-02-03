# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:37:45 2020

@author: Nayanika Borah
"""
#to check if both tuples are of equal length
t=()
t= eval (input("enter a sequence"))
T=()
T= eval (input("enter a sequence"))
l=len(t)
for i in range (0,l):
    if t[i]== T[i]:
        f=1
    else:
        f=0
        break
if f==1:
    print("true")
else:
    print("false")