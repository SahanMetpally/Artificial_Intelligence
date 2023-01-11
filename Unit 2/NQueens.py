#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from heapq import heappush, heappop, heapify
from random import randrange
import random

def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True

def make_list():
    for i in range(0,n):
        sett.add(i)
    x = int(n/2)
    liste.append(x)
    for i in range(1,x+1):
        if x-i >= 0:
            liste.append(x-i)
        if x+i < n:
            liste.append(x+i)

def goal_test(state):
    for row in state:
        if row == None:
            return False
    return True

def get_next_unassigned(i):
     return liste[i]

def fill_board(state, pos, row):
    dis = abs(row-pos)
    pos1 = state[pos]
    return {pos1, pos1-dis, pos1+dis}

def calc(l,r,t,b):
    h = 0
    if l > t:
        h+= t
    elif l != 0:
        h += l
    if r > t:
        h += t
    elif r != 0:
        h+= r
    if l > b:
        h += b
    elif l != 0:
        h += l
    if r > b:
        h += b
    elif r != 0:
        h += r
    return h

def get_sorted_values(state,var):
    settt = sett.copy()
    for i in range(0,n):
        if state[i] != None:
            pos1 = state[i]
            dis = abs(var-i)
            settt.difference_update({pos1, pos1-dis, pos1+dis})
        if not settt:
            return None
    heap_list = []
    for s in settt:
        l = s
        r = n-1-s
        t = var
        b = n-1-var
        h = calc(l,r,t,b)
        tuple1 = (h, s)
        heappush(heap_list, tuple1)
    return heap_list
            
    
def csp_backtracking(state, vare):
    if None not in state:
        return state
    var = get_next_unassigned(vare)
    t = get_sorted_values(state, var)
    while t:
        x = heappop(t)
        val = x[1]
        temp = state.copy()
        temp[var] = val
        result = csp_backtracking(temp,vare+1)
        if result is not None:
            return result
    return None

def generateFlawed(state2,n):
    for i in range(0,n):
        var = get_next_unassigned(i)
        heap_list = []
        for s in sett:
            h = calc2(state2, var, s)
            tuple1 = (h, s)
            heappush(heap_list, tuple1)
        y = heappop(heap_list)[1]
        state2[var] = y
    return state2
        

def calc2(state2, row, col):
    h = 0
    for i in range(0,n):
        if state2[i] == col and i != row:
            h += 1

    for i in range(1, n):
        if row+i < n:
            if state2[row+i] == col+i:
                h += 1
            if state2[row+i] == col-i:
                h+= 1
        if row - i >= 0:
            if state2[row-i] == col+i:
                h += 1
            if state2[row-i] == col-i:
                h += 1
        if row + i > n and row - i < 0:
            break
    return h

def calc3(state2, row, col):
    h=0
    for i in range(0,n):
        x = state2[i]
        if abs(row-i) == abs(col-x) or x == col:
            h+= 1
    h -= 1
    return h
                
def increment_repair(states):
    heap_list = []
    for i in range(0,n):
        h = calc3(states, i, states[i])
        tuple1 = (0-h, i)
        heappush(heap_list,tuple1)
    listP = []
    temp = heappop(heap_list)
    if temp[0] == 0:
        return states
    listP.append(temp[1])
    while heap_list:
        a = heappop(heap_list)
        if a[0] == temp[0]:
            listP.append(a[1])
        else:
            break
    rand = random.choice(listP)
    
    listS = []
    minI = 0
    minV = n
    for i in range(0,n):
        y = calc3(states, rand, i)
        if y == minV:
            listS.append(i)
        if y < minV:
            listS = []
            minV = y
            listS.append(i)
            
    minI = random.choice(listS)
    st = states.copy()
    st[rand] = minI
    result = increment_repair(st)
    return result


def equation(n):
    count = 0
    lit = []
    for i in range(1,n,2):
        lit.append(i)
        count += 1
    for i in range(0,n,2):
        lit.append(i)
        count += 1
    return lit



total = 0.0
listSolutions = []
n = 8
while n < 201:
    liste = []
    sett = set()
    print(n)
    print(total)

    if n%6!= 2 and n%6 != 3:
        start = time.perf_counter()
        solution1 = equation(n)
        end = time.perf_counter()
        total += (end-start)
        listSolutions.append(solution1)
    elif n < 25:
        make_list()
        state = [None]*n
        start = time.perf_counter()
        solution = csp_backtracking(state, 0)
        end = time.perf_counter()
        total += (end-start)
        listSolutions.append(solution)
    else:
        make_list()
        state2 = generateFlawed([None]*n, n)
        start = time.perf_counter()
        solution2 = increment_repair(state2.copy())
        end = time.perf_counter()
        total += (end-start)
        listSolutions.append(solution2)
    

    n += 1
n = 8
cCount = 0
for i in range(0,len(listSolutions)):
    correct = (test_solution(listSolutions[i]))
    if correct:
        cCount += 1
        print(str(correct) + " " + str(n) + " is correct!")
    else:
        print(str(correct) + " " + str(n) + " is incorrect!")
    n += 1
    print()

print(str(cCount) + " out of " + str(n-8) + " in " + str(total) + " seconds!")




