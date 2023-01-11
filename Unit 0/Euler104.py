#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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