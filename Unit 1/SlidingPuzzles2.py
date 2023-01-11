#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from collections import deque
from heapq import heappush, heappop, heapify

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

def stringify(string):
    string = string.replace("1", "A")
    string = string.replace("2", "B")
    string = string.replace("3", "C")
    string = string.replace("4", "D")
    string = string.replace("5", "E")
    string = string.replace("6", "F")
    string = string.replace("7", "G")
    string = string.replace("8", "H")
    string = string.replace("9", "I")
    return string

def checkParity(string, length):
    pos = string.find(".")
    string = string.replace(".", "")
    if(length <= 9):
        string = stringify(string)
    chars = list(string)
    count = 0
    for i in range(len(chars)):
        for j in range(i+1, len(chars)):
            if(ord(chars[i]) > ord(chars[j])):
                count += 1
    if((length**0.5)%2 == 0):
        pos = int(pos/(length**0.5))
        if(pos%2 == 0):
            if(count%2 == 1):
                return True
        else:
            if(count%2 == 0):
                return True
    else:
        if(count%2 == 0):
            return True
    return False

def solve(str, goal):
    num, dicte= BFS(str, goal)
    count = 0
    if(num == 0):
        print("No Answer")
    else:
        val = num
        while val != str:
            #print(dicte[val])
            val = dicte[val]
            count += 1
    return count


def kDFS(start, depth, goal):
    set = {"1"}
    queue = deque()
    set.add(start)
    tuple = (start, 0, set)
    queue.append(tuple)
    
    while len(queue) != 0:
        
        tuple = queue.pop()
        temp = tuple[0]
        if(temp == goal):
            return tuple[1]
        if(int(tuple[1]) < depth):
            answers = get_children(int(len(temp)**0.5), temp).split(" ")
            for children in answers:
                set = tuple[2].copy()
                if not children in set:
                    set.add(children)
                    tuple2 = (children, tuple[1]+1, set)
                    if(children == goal):
                        return tuple2[1]
                    queue.append(tuple2)
    return None


def IDDFS(string, goal):
    max_depth = 0
    answer = None
    while answer == None:
        answer = kDFS(string, max_depth, goal)
        max_depth += 1
    return answer

def findDistance(x,y,size):
    a = abs(int(x/size) - int(y/size))
    b = abs(int(x%size) - int(y%size))
    return (a+b)

def Taxicab(string):
    count = 0
    size = int(len(string)**0.5)
    if(size < 4):
        string = stringify(string)
    if size >= 2:
        count += findDistance(string.index("A"), 0, size)
        count += findDistance(string.index("B"), 1, size)
        count += findDistance(string.index("C"), 2, size)
    if size >= 3:
        count += findDistance(string.index("D"), 3, size)
        count += findDistance(string.index("E"), 4, size)
        count += findDistance(string.index("F"), 5, size)
        count += findDistance(string.index("G"), 6, size)
        count += findDistance(string.index("H"), 7, size)
    if size >= 4:
        count += findDistance(string.index("I"), 8, size)
        count += findDistance(string.index("J"), 9, size)
        count += findDistance(string.index("K"), 10, size)
        count += findDistance(string.index("L"), 11, size)
        count += findDistance(string.index("M"), 12, size)
        count += findDistance(string.index("N"), 13, size)
        count += findDistance(string.index("O"), 14, size)
    if size >= 5:
        count += findDistance(string.index("P"), 15, size)
        count += findDistance(string.index("Q"), 16, size)
        count += findDistance(string.index("R"), 17, size)
        count += findDistance(string.index("S"), 18, size)
        count += findDistance(string.index("T"), 19, size)
        count += findDistance(string.index("U"), 20, size)
        count += findDistance(string.index("V"), 21, size)
        count += findDistance(string.index("W"), 22, size)
        count += findDistance(string.index("X"), 23, size)
    return count


def a_star(string, goal):
    set = {"1"}
    start = string
    depth = 0
    taxi = Taxicab(start) + depth
    tuple = (taxi, depth, start)
    heap_list = []
    heappush(heap_list, tuple)
    while heap_list:
        tuple2 = heappop(heap_list)
        if(tuple2[2] == goal):
            return tuple2[1]
        temp = tuple2[2]
        if temp not in set:
            set.add(temp)
            answers = get_children(int(len(temp)**0.5), temp).split(" ")
            for children in answers:
                if children not in set:
                    state = children
                    d = tuple2[1] + 1
                    tc = d + Taxicab(state)
                    tuple3 = (tc, d, state)
                    heappush(heap_list, tuple3)
    return None
                    
    

fileName = sys.argv[1]

file = open(fileName)
i = 0

for line in file:
    a = int(line.split( )[0])
    s = line.strip().split(" ")[1].strip()  #.split( )[1]
    algo = line.strip().split(" ")[2].strip()
    goal = find_goal(s)
    
    start = time.perf_counter()
    bool = checkParity(s, int(len(s)))
    end = time.perf_counter()
    if not bool:
        print("Line " + str(i) + ":" + str(s) + " " + "No Solution determined in " + str(end-start) + " seconds")
    
    elif algo == "B":
        start = time.perf_counter()
        solved = solve(s, goal)
        end = time.perf_counter()
        print("Line " + str(i) + ": " + str(s) + ", BFS - " + str(solved) + " moves found in " + str((end - start)) + " seconds")
    
    elif algo == "I":
        start = time.perf_counter()
        solved2 = IDDFS(s, goal)
        end = time.perf_counter()
        print("Line " + str(i) + ": " + str(s) + ", ID-DFS - " + str(solved2) + " moves found in " + str((end - start)) + " seconds")
    
    elif algo == "A":    
        start = time.perf_counter()
        solved3 = a_star(s, goal)
        end = time.perf_counter()
        print("Line " + str(i) + ": " + str(s) + ", A* - " + str(solved3) + " moves found in " + str((end - start)) + " seconds")
    
    else:
        start = time.perf_counter()
        solved = solve(s, goal)
        solved2 = IDDFS(s, goal)
        solved3 = a_star(s, goal)
        end = time.perf_counter()
        print("Line " + str(i) + ": " + str(s) + ", BFS - " + str(solved) + " moves found in " + str((end - start)) + " seconds")
        print("Line " + str(i) + ": " + str(s) + ", ID-DFS - " + str(solved2) + " moves found in " + str((end - start)) + " seconds")
        print("Line " + str(i) + ": " + str(s) + ", A* - " + str(solved3) + " moves found in " + str((end - start)) + " seconds")
        
    print()
    i+=1
    
    
    
    