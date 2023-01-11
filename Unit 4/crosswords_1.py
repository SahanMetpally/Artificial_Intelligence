#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

size = sys.argv[1]

pos = size.find("x")

height = size[0:pos]
width = size[pos+1:]

blocked = sys.argv[2]
filename = sys.argv[3]

length = len(sys.argv)

for i in range(4, length):
    string = sys.argv[i]
    
    direction = string[0]
    pos = size.find("x")
    
    string = string[1:]
    
    row = string[0:pos]
    
    string = string[pos+1:]
    
    