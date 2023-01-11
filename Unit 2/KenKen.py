#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time

fileName = sys.argv[1]
file = open(fileName)

puzzle = ""
constraints = []
neighbors = {}
symbol_set = set()
groups = {}
matrix = {}
solved = set()
liste = []
checks = {}
for line in file:
    liste.append(line.rstrip("\n"))

puzzle = liste[0]
N = int(len(puzzle)**0.5)

for i in range(1,N+1):
    symbol_set.add(i)

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
for i in range(0, N*N):
        sett = set()
        for s in constraints:
            if i in s:
                sett = sett|s
        sett.remove(i)
        neighbors[i] = sett

for i in range(0, len(puzzle)):
    if puzzle[i] in groups:
        groups[puzzle[i]].add(i)
    else:
        groups[puzzle[i]] = set()
        groups[puzzle[i]].add(i)
state = "."*len(puzzle)

for i in range(0, len(state)):
    temp = symbol_set.copy()
    matrix[i] = temp

while len(liste) > 1:
    s = liste.pop(1)
    sett = []
    x = s.split(" ")
    sett.append(x[1])
    sett.append(x[2])
    checks[s[0]] = sett
    
def get_next_unassigned(state, solve, m):
    shortest = len(state)
    minI = 0
    for key in groups:
        x = len(groups[key])
        if x < shortest and key not in solve:
            shortest = x
            minI = key
    return minI

def get_sorted_values(t,mat):
    return mat[t]

# =============================================================================
# def forward_looking(mat, index, val, state):
#     for i in neighbors[index]:
#         mat[i].discard(val)
#         if(len(mat[i]) == 0):
#             return None
#     return state
# =============================================================================
def forward_looking(state, var, solve, mat):
    liste = []
    liste.append(var)
    while liste:
        var = liste.pop(0)
        mat[var] = set(state[var])
        for i in neighbors[var]:
            if state[var] == state[i]:
                return None
            if int(state[var]) in mat[i]:
                mat[i].remove(int(state[var]))
            if len(mat[i]) == 0 and i not in solve:
                return None
    return state

def value(vals, oper, sol):
    ans = 0
    if oper == "+":
        for val in vals:
            ans += val
    elif oper == "x":
        ans = 1
        for val in vals:
            ans *= val
    elif oper == "-":
        ans = abs(vals[0]-vals[1])
    else:
        a = vals[0]
        b = vals[1]
        if b > a:
            ans = b/a
        else:
            ans = a/b
    if ans == sol:
        return True
    else:
        return False
            
def check(index,state2):
    var = puzzle[index]
    s = groups[var]
    what = checks[var]
    sol = int(what[0])
    calc = what[1]
    sett = []
    for i in s:
        if state2[i] == ".":
            return True
        else:
            sett.append(int(state2[i]))
    return value(sett, calc, sol)
    
    
def csp_backtracking(state, solve, m):
    #if state[0] == "4" and state[3] == "1":
    #print(state)
    if "." not in state:
        return state
    var = state.index(".")
    t = m[var]
    for val in t:
        s = solve.copy()        
        mat = {x: m[x].copy() for x in m}
        state2 = state[0:var] + str(val) + state[var+1:]
        s.add(var)
        r = forward_looking(state2, var, s, mat)
        if r is not None:
            if check(var, state2):
                result = csp_backtracking(state2, s, mat)
                if result is not None:
                    return result
    return None
def print_board(state):
    for i in range(0, int(len(state)**0.5)):
        for j in range(0+i*int(len(state)**0.5), 0+i*int(len(state)**0.5) + int(len(state)**0.5)):
            print(state[j], end = " ")
        print()
        
#print_board(puzzle)
start = time.perf_counter()

solution = csp_backtracking(state, solved, matrix)

end = time.perf_counter()
total = (end-start)
print(solution)
print(str(total) + " seconds!")