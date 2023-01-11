#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
from collections import deque



fileName = "words_06_letters.txt"
dicte = {}
file = open(fileName)

for line in file:
    a = line.strip()
    dicte[a] = "e"

def get_children(start):
    l = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    letters = l.split(" ")
    children = ""
    for index in range(0, len(start)): 
        for letter in letters:
            temp = start[:index] + letter + start[index + 1:]
            if temp in dicte and temp != start:
                children = children + " " + temp
    return children
            
def BFS(string, goal):
    dicte2 = {}
    queue = deque()
    set = {'1'}
    set.add(string)
    queue.append(string)
    while len(queue) != 0:
        temp = queue.popleft()
        if(temp == goal):
            return temp, dicte
        answers = get_children(temp).strip().split(" ")
        for children in answers:
            if not children in set:
                dicte2[children] = temp
                if(children == goal):
                    return children, dicte2
                set.add(children)
                queue.append(children)
    return 0, dicte2

def solve(start, end):
    num, dicte3= BFS(start, end)
    count = 0
    path = ""
    if(num == 0):
        return 0, 0
    else:
        val = num
        path += val + " "
        while val != start:
            #print(dicte[val])
            val = dicte3[val]
            count += 1
            path += val + " "
    return count, path

max = 0
words = ""

length, path = solve("crafty", "dimmed")

pathway = path.strip().split(" ")
pathway.reverse()
for word in pathway:
    print(word)
# =============================================================================
# for key in dicte:
#     set = {'1'}
#     set.add(key)
#     queue = deque()
#     queue.append(key)
#     temp = ""
#     while len(queue) != 0:
#         temp = queue.popleft()
#         children = get_children(temp).strip().split(" ")
#         for child in children:
#             if not child in set:
#                 set.add(child)
#                 queue.append(child)
#     if len(set) == 1626:
#         length, path = solve(key, temp)
#         if length > max:
#             max = length
#             words = key + " " + temp
#             print(max)
#             print(words)
# =============================================================================
        