# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 20:20:38 2020

@author: Nayanika Borah
"""
print("welcome to trivia")

ans = input("are you ready to play? (y/n)")
score = 0
total_q = 4
if ans.lower() == "y":
    ans = input("what is my name?")
    if ans.lower() =="jerry":
        score +=1 
        print("correct")
    else :
        print("incorrect")
        
    ans = input("whats my age?")
    if ans =="18":
        score += 1
        print("correct")
    else:
        print("incorrect")
    ans = input("whats the thing i like the most?")
    if ans.lower()=="anime":
        score += 1
        print("correct")
    else: 
        print("incorrect")
    ans = input("whats the name of the most beautiful yet  dangerous girl i know?")
    if ans.lower() =="majoni baa":
        score += 1
        print("correct")
    else: 
        print("incorrect")
print("thank you for playing, you got",score,"answers correctly")