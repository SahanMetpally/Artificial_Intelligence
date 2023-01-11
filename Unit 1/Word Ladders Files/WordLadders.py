#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
from collections import deque



fileName = "words_06_longer.txt" #sys.argv[1]
dicte = {}
file = open(fileName)

start = time.perf_counter()
size = 0
for line in file:
    size += 1
    a = line.strip()
    dicte[a] = "e"
    
    
end = time.perf_counter()
print("Time to create the data structure was: " + str(end-start))
print("There are " + str(size) + " words in this dict.")
print()

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

    

filename = sys.argv[2]
file = open(filename)
i = 0
t = float(0.0)

for line in file:
    startW = line.split(" ")[0].strip()
    endW = line.split(" ")[1].strip()
    
    start = time.perf_counter()
    length, path = solve(startW, endW)
    end = time.perf_counter()

    t  = t + float(end-start)
    
    print("Line: " + str(i))
    i += 1
    if path == 0:
        print("No Solution!")
    else:
        print("Length is: " + str(length+1))
        pathway = path.strip().split(" ")
        pathway.reverse()
        for word in pathway:
            print(word)
    print()
print("Time to solve all of these puzzles was: " + str(t) + " seconds")
