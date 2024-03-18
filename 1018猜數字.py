# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random


def timeTable(a,b):
 
 for c in range(1,a+1):
    for i in range(1,b+1):
       print(c,"X",i,"=",c*i,"\t",sep="",end="")
    print("")
 return c,i,c*i


def playGame():
    #gen random num 1-100
    target=random.randint(1,100)
    #try to guess the number until you get it
    while True:
        ans = int(input('enter your anser:'))
        if(target==ans):
            print('猜對了')
            break
        elif(target>ans):
             print('太小了!')
        elif(target<ans):
             print('太大了!')
        
def main():
    playGame()

main()
