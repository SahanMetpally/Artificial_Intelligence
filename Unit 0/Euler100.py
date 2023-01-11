#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time


for j in range(1070379110400, sys.maxsize):
    for i in range(756872327400, j):
        prob = (i/j)*((i-1)/(j-1))        
        if prob == 0.5:
            print(i)
            sys.exit()
        if prob > 0.5:
            break