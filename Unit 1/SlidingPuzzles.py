#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from collections import deque

def find_goal(s):
    s = "".join(sorted(s))
    s = s[1:]
    s += "."
    return s
    
def print_puzzle(a, s):
    while s != "":
        print(s[:a])
        s = s[a:]
    print()
    
def swap(a, b, s):
    s = list(s)
    s[a], s[b] = s[b], s[a]
    return "".join(s)
    
def get_children(a, s):
    x = a*a
    pos = s.find(".")
    answers = ""
    if(pos-1 >= 0 and pos%a != 0):
        #print(swap(pos, pos-1, s))
        answers += swap(pos, pos-1, s) + " "

    if(pos+1 < x and pos%a != a-1):
        #print(swap(pos, pos+1, s))
        answers += swap(pos, pos+1, s) + " "

    if(pos-a >= 0):
        #print(swap(pos, pos-a, s))
        answers += swap(pos, pos-a, s) + " "

    if(pos+a < x):
        #print(swap(pos, pos+a, s))
        answers += swap(pos, pos+a, s) + " "
    return answers.strip()
        
def BFS(string, goal):
    dicte = {}
    queue = deque()
    set = {'1'}
    set.add(string)
    queue.append(string)
    while len(queue) != 0:
        temp = queue.popleft()
        if(temp == goal):
            return temp, dicte
        answers = get_children(int(len(temp)**0.5), temp).split(" ")
        for children in answers:
            if not children in set:
                dicte[children] = temp
                if(children == goal):
                    return children, dicte
                set.add(children)
                queue.append(children)
    return 0, dicte

def solve(str):
    num, dicte= BFS(str, find_goal(str))
    if(num == 0):
        print("No Answer")
    else:
        count = 0
        val = num
        while val != str:
            #print(dicte[val])
            val = dicte[val]
            count += 1
    return count

#solve("A.CB")

fileName = sys.argv[1]

file = open(fileName)
i = 0

for line in file:
    a = int(line.split( )[0])
    s = line.split( )[1]
    #print("Line " + str(i) + " Start State: ")
    #print_puzzle(a, s)
    #print("Line " + str(i) + " Goal State: ")
    #answer = find_goal(a,s)
    #print(answer + "\n")
    #print("Line " + str(i) + " Children: ")
    #get_children(a, s)
    #print()
    start = time.perf_counter()
    solved = solve(s)
    end = time.perf_counter()
    print("Line " + str(i) + ": " + str(s) + ", " + str(solved) + " moves found in " + str((end - start)) + " seconds")
    i+=1
    
    
    
    