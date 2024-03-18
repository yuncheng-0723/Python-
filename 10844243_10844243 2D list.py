# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

#myInLine = open('test.txt' , 'r')
#for line in myInLine:
   # nums = line.split()
    #for num in nums:
      # print(num)
list1 = []
list2 = []
for i in range(5):
    for j in range(5):
        list1.append(random.randint(1, 9))
    list2.append(list1)
    list1 = []
print(list2)

for i in range(5):
    for j in range(5):     
        print(list2[i][j], " ", end="")
    print("")
    
list3 = []
for i in range(9):
    list3.append(0)
for i in range(5):
    for j in range(5): 
        list3[list2[i][j]-1]+=1
print(list3)
for i in range(9):
    print(i+1, '\ s= ', list3[i])