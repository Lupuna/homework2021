# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:41:00 2021

@author: terra
"""
import random

file1 = open ('task1.txt', 'r')
randoms = []

for row in file1:
    if int(row) < 2020:
        randoms.append (row)
        print (randoms)

n = len(randoms)        

for g in range(0, n):
    for i in range(0, n):
        for k in range(0, n):
            g = random.choice(randoms)
            i = random.choice(randoms)
            k = random.choice(randoms)
            if int(g)+int(i)+int(k) == 2020:
                print (int(g)*int(i)*int(k))
                file2 = open ('output1.txt', 'w')
                file2.write(str(int(g)*int(i)*int(k)))
                

                
        

                
        

