#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time

constraints = []
neighbors = {}
board ="hi"
symbol_set = set()
def find_constraints(N, subW, subH):
    for i in range(0, N):
        sett = set()
        for j in range(0, N):
            sett.add(i*N + j)
        constraints.append(sett)
    for i in range(0, N):
        sett = set()
        for j in range(0, N):
            sett.add(i + N*j)
        constraints.append(sett)
    temp = set()
    for i in range(0,int(N/subW)):
        x = int(subW*i)
        temp.add(x)
        for j in range(0, int(N/subH)-1):
            x += int(subH*N)
            temp.add(x)
    for s in temp:
        sett = set()
        x = s-1
        for i in range(0,subW):
            x += 1
            sett.add(x)
            y = x
            for i in range(1,subH):
                y += N
                sett.add(y)
        constraints.append(sett)
    for i in range(0, N*N):
        sett = set()
        for s in constraints:
            if i in s:
                sett = sett|s
        sett.remove(i)
        neighbors[i] = sett

def print_board(board):
    for i in range(0, N):
        for j in range(0+1*i, 0+1*i + N):
            print(board[j], end = " ")
        print()
        
def get_next_unassigned(state):
     return state.index(".")

def get_sorted_values(t, state):
    temp = symbol_set.copy()
    for i in neighbors[t]:
        if state[i] != "." and not state[i].isalpha():
            temp.discard(int(state[i]))
        elif state[i].isalpha():
            temp.discard(state[i])
    return temp
    
def csp_backtracking(state):
    if "." not in state:
        return state
    var = get_next_unassigned(state)
    t = get_sorted_values(var, state)
    for val in t:
        state = state[0:var] + str(val) + state[var+1:]
        result = csp_backtracking(state)
        if result is not None:
            return result
    return None

def counter(state):
    dicte = {}
    for i in symbol_set:
        count = 0
        for s in state:
            if s == str(i):
                count += 1
        dicte[i] = count
    return dicte

fileName = sys.argv[1]
 
file = open(fileName)
total = 0.0
for line in file:
    start = time.perf_counter()
    symbol_set = set()
    constraints = []
    neighbors = {}
    
    line = line.strip()
    board = line
    l = len(line)
    N = int(l**0.5)
    subH = 0
    subW = 0
    if N**0.5%1 == 0:
        subH = subW = int(N**0.5)
    else:
        for i in range(int(N**0.5)+1, N):
            if N%i == 0:
                subW = i
                break
        for i in range(int(N**0.5), 1, -1):
            if N%i == 0:
                subH = i
                break
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if N <= 9:
        for i in range(1,N+1):
            symbol_set.add(i)
    elif N > 9:
        for i in range(1,10):
            symbol_set.add(i)
        for i in range(0, N-9):
            symbol_set.add(string[i])
    find_constraints(N, subW, subH)
    solution = csp_backtracking(line)
    #s = counter(solution)
    end = time.perf_counter()
    total += (end-start)
    print(solution)
print(str(total) + " seconds!")
