# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:31:32 2020

@author: Nayanika Borah
"""
#printing a sequence of letters

for a in range (1,6):

    for b in range (65,65+a):
      ch= chr(b)
      print (ch, end=" ")
    print ("\n")
    