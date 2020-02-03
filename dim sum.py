# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 18:42:02 2020

@author: Nayanika Borah
"""

#sum of numbers in a tuple
t=()
t=eval(input("enter a sequence"))
l=len(t)
s=0
for a in range (0,l):
    
    s=s+t[a]
print ("sum = ",s)