#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

sett = set()
settL = set()

def is_prime(x):
    if(x in sett):
        return True
    elif(x in settL):
        return False
    prime = True
    y = int(x**0.5)
    if(x ==1):
        settL.add(x)
        return False
    if(x != 2):
        if(x%2 == 0):
            settL.add(x)
            return False
    for i in range(3, y+1):
        if(x%i == 0):
            settL.add(x)
            return False
        i += 1
    if(prime):
        sett.add(x)
    else:
        settL.add(x)
    return prime
        
answer = 1
for n in range(99996, sys.maxsize, 12):
    x = n*n
    count = 0
    if n == 180180:
        print("here")
    if(answer >= 2000):
        print(str(n-12))
        break     
    answer = 1
    for divisor in range(2, sys.maxsize):
        if(is_prime(divisor)):
            while(x%divisor == 0):
                x = x/divisor
                count += 1
    
        answer = answer * (count + 1)
    
        if x == 1:
            break
        
        count = 0    
