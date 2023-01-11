#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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