#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def pascal(row, i):
    if i == 1 or i == row:
        return 1
    if i > row:
        return 0
    return pascal(row-1, i-1) + pascal(row-1, i)
    

#print(pascal(90,90))

def grid(x,y):
    if x == 0:
        return 1
    if y == 0:
        return 1
    return 2 + grid(x-1,y) + grid(x,y-1)

grid(3,4)

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

fib(6)