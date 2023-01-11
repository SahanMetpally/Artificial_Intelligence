#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from collections import deque
from heapq import heappush, heappop, heapify



letters = {
    "A": "0 0",
    "B": "0 1",
    "C": "0 2",
    "D": "0 3",
    "E": "1 0",
    "F": "1 1",
    "G": "1 2",
    "H": "1 3",
    "I": "2 0",
    "J": "2 1",
    "K": "2 2",
    "L": "2 3",
    "M": "3 0",
    "N": "3 1",
    "O": "3 2",
    "P": "3 3"
    }

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
    sett = set()
    length = a*a
    pos = s.find(".")
    if(pos-1 >= 0 and pos%a != 0):
        sett.add(swap(pos, pos-1, s))
        
    if(pos+1 < length and pos%a != a-1):
        sett.add(swap(pos, pos+1, s))

    if(pos-a >= 0):
        sett.add(swap(pos, pos-a, s))

    if(pos+a < length):
        sett.add(swap(pos, pos+a, s))

    return sett

def Taxicab(string):
    count = 0
    for i in range(0, 16):
        if string[i] != ".":
            count += abs(int((i)/4) - int(letters[string[i]][0]))
            count += abs(int((i)%4) - int(letters[string[i]][2]))
    return count


def collisions(string):
    rows = [(string[i:i+4]) for i in range(0, len(string), 4)] 
    count = 0
    for x in range(0,4):
        str_list = []
        str_list2 = []
        row = rows[x]
        col = rows[0][x] + rows[1][x] + rows[2][x] + rows[3][x]
        
        for l in range(0,4):
            if int((ord(row[l])-65)/4) == x:
                str_list.append(row[l])
            if int((ord(col[l])-65)%4) == x and col[l] != ".":
                str_list2.append(col[l])
        
        l1 = len(str_list)-1
        l2 = len(str_list2)-1
        for x in range(0, 3):
            if(l2 > x): 
                if(ord(str_list2[x]) > ord(str_list2[x+1])):
                    count += 2
            if(l1 > x): 
                if(ord(str_list[x]) > ord(str_list[x+1])):
                    count += 2

    return count

def SpecificCollisionR(string, x):
    temp = []
    for x in string:
        if int((ord(x)-65)/4) == x:
            temp.add(x)
    a = len(temp)-1
    count = 0
    for i in range(0, a):
        if(ord(temp[i]) > ord(temp[i+1])):
            count += 2
    return count

def SpecificCollisionC(string, x):
    string1 = []
    for x in string:
        if int((ord(x)-65)%4) == x:
            string1.add(x)
    a = len(string1)-1
    count = 0
    for i in range(0, a):
        if(ord(string1[i]) > ord(string1[i+1])):
            count += 2
    return count

def a_star(string, goal):
    set = {"1"}
    start = string
    depth = 0
    colli = collisions(string)
    taxi = Taxicab(start) + depth + colli
    #print(str(start) + ": " + str(taxi))
    tuple = (taxi, depth, start, colli)
    heap_list = []
    heappush(heap_list, tuple)
    while heap_list:
        tuple2 = heappop(heap_list)
        if(tuple2[2] == goal):
            return tuple2[1]
        temp = tuple2[2]
        if temp not in set:
            set.add(temp)
            answers = get_children(4, temp)
            for children in answers:
                if children not in set:
                    state = children
                    d = tuple2[1] + 1
                    
                    x = children.index(".")
                    rep = children.index(temp[x])
                    replaced = x
                    y = int(letters[temp[replaced]][0])
                    z = int(letters[temp[replaced]][2])
        
                    D1 = abs(int((rep)/4) - (y)) + abs(int((rep)%4) - (z))
                    D2 = abs(int((replaced)/4) - (y)) + abs(int((replaced)%4) - (z))
                    diff = D1 - D2
                    
# =============================================================================
#                     pCols = 0
#                     cCols = 0
#                       
#                     for i in range(0,4):
#                         a = children[i*4:i*4+4]
#                         b = temp[i*4:i*4+4]
#                         c = children[i:16:4]
#                         d1 = temp[i:16:4]
#                         if(a != b):
#                              pCols += SpecificCollisionR(b, i)
#                              cCols += SpecificCollisionR(a, i)
#                         if(c != d1):
#                              pCols += SpecificCollisionC(d1, i)
#                              cCols += SpecificCollisionC(c, i)
# =============================================================================

                    cols = collisions(state)
                    #cols = cCols - pCols
                    tc = tuple2[0] + cols + 1 + diff - tuple2[3]
                    tuple3 = (tc, d, state, cols)
                    heappush(heap_list, tuple3) 
    return None



fileName = "15_puzzles.txt" #sys.argv[1]

file = open(fileName)
i = 0
total = 0.0
for line in file:
    s = line.strip() #.split( )[1]
    goal = find_goal(s)
 
    start = time.perf_counter()
    solved3 = a_star(s, goal)
    end = time.perf_counter()
    print("Line " + str(i) + ": " + str(s) + ", A* - " + str(solved3) + " moves found in " + str((end - start)) + " seconds")
    total += end-start
    print(total/60)
    i+=1
print(total)
    
    
    
    