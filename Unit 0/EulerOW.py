#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time


        
#Euler 102
print("Euler 102:")

def area(x1, y1, x2, y2, x3, y3):
    return abs(((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2.0));

def check(x1, y1, x2, y2, x3, y3, x4, y4):
    A = area(x1,y1,x2,y2,x3,y3);
    A1 = area(x1,y1,x2,y2,x4,y4);
    A2 = area(x1,y1,x3,y3,x4,y4);
    A3 = area(x2,y2,x3,y3,x4,y4);
    
    if(A > (A1 + A2 + A3 - 0.001) and A < (A1 + A2 + A3 + 0.001)):
        return True
    else:
        return False

fileName = "triangles.txt"

file = open(fileName)
i = 0
for line in file:
    s = line.split(",")
    Ax = int(s[0])
    Ay = int(s[1])
    Bx = int(s[2])
    By = int(s[3])
    Cx = int(s[4])
    Cy = int(s[5])
    
    Ox = 0
    Oy = 0
    
    if(check(Ax, Ay, Bx, By, Cx, Cy, Ox, Oy)):
        i += 1

print(i)

print()
#Euler 104
print("Euler 104")

a = 1
b = 1
c = 1
  
i = 2
 
while True:
    i += 1
 
    c = b + a
    tail = c%1000000000
    if ("".join(sorted(str(tail))) == "123456789"):
        head = str(c)[0:9]
        if ("".join(sorted(str(head))) == "123456789"):
            break            
    a = b
    b = c

print(i)

print()
#Euler 108
print("Euler 108")

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
        
print()
#Euler 100
print("Euler 100")
10
for j in range(1070379110400, sys.maxsize):
    for i in range(756872327400, j):
        prob = (i/j)*((i-1)/(j-1))        
        if prob == 0.5:
            print(i)
            sys.exit()
        if prob > 0.5:
            break