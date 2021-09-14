# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
a = float (input ("Ведите длину стороны а:" ))
b = float (input ('Ведите длину стороны в:' ))
cos = float (input ('Введите значение угла между сторонами:' ))
if cos >1 :
    print (math.sqrt(a**2 + b**2 - 2 * math.cos(math.degrees(cos)) * a * b))
elif cos >=0 and cos < 1:
    print (math.sqrt(a**2 + b**2 - 2 * cos * a * b))
else:
    print ('Я не умею это считать.')
input ()