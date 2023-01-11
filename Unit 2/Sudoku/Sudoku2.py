#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time

constraints = []
neighbors = {}
board ="hi"
symbol_set = set()
matrix = {}
solved = set()

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
        for j in range(0+i*N, 0+i*N + N):
            print(board[j], end = " ")
        print()
        
def get_next_unassigned(state, solve, m):
    shortest = len(state)
    minI = 0
    for key in m:
        x = len(m[key])
        if x < shortest and key not in solve:
            shortest = x
            minI = key
    return minI

def get_sorted_values(t, state, mat):
    return mat[t]

def forward_looking(state, var, solve, mat):
    liste = []
    liste.append(var)
    while liste:
        var = liste.pop(0)
        mat[var] = set(state[var])
        for i in neighbors[var]:
            if state[var] == state[i]:
                return None
            if state[var] in mat[i]:
                mat[i].remove(state[var])
            if len(mat[i]) == 1 and i not in solve:
                for x in mat[i]:
                    break
                state = state[0:i] + str(x) + state[i+1:]
                solve.add(i)
                liste.append(i)
# =============================================================================
#             print_board(state)
#             print(i)
#             print(solve)
#             print()
# =============================================================================
            if len(mat[i]) == 0 and i not in solve:
                #print("NONE")
                return None
    return state

def constraint_propogation(state, m, solve):
    for sets in constraints:
        count = 0
        index = 0
        for var in symbol_set:
            for vals in sets:
                if var in m[vals]:
                    count += 1
                    index = vals
            if count == 0 or state == None:
                return None
            if count == 1:
                count = 0
                state = state[0:index] + str(var) + state[index+1:]
                solve.add(index)
                if "." not in state:
                    return state
                state = forward_looking(state, index, solve, m)

            count = 0
            index = 0
    return state

def csp_backtracking(state, solve, m):
    if "." not in state:
        return state
    var = get_next_unassigned(state, solve, m)
    t = m[var]
    for val in t:
        s = solve.copy()        
        mat = {x: m[x].copy() for x in m}
        state = state[0:var] + str(val) + state[var+1:]
        s.add(var)
        if "." not in state:
            return state
        r = forward_looking(state, var, s, mat)      
        if r is not None:
            r = constraint_propogation(r, mat, s)
            
        if r is not None:
            result = csp_backtracking(r, s, mat)
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

def make_board(state):
    oneS = set()
    for i in range(0,len(state)):
        if state[i] in symbol_set:
            matrix[i] = set(state[i])
            solved.add(i)
        else:
            temp = symbol_set.copy()
            for j in neighbors[i]:
                x = str(state[j])
                if x in temp:
                    temp.remove(x)
            matrix[i] = temp
            if len(temp) == 1:
                 oneS.add(i)
                 
    for i in oneS:
        for val in matrix[i]:
            solved.add(i)
            state = state[0:i] + str(val) + state[i+1:]
            state = forward_looking(state, i, solved, matrix)
    state = constraint_propogation(state, matrix, solved)
    return state

fileName = "sudoku_puzzles_all.txt"
number = 0
file = open(fileName)
total = 0.0
for line in file:
    #print(number)
    #print(line)
    #number += 1
    
    symbol_set = set()
    constraints = []
    neighbors = {}
    matrix = {}
    solved = set()
    
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
            symbol_set.add(str(i))
    elif N > 9:
        for i in range(1,10):
            symbol_set.add(str(i))
        for i in range(0, N-9):
            symbol_set.add(string[i])
    start = time.perf_counter()
    find_constraints(N, subW, subH)

    line = make_board(board)

    #print(line)
    solution = csp_backtracking(line, solved, matrix)
    #print(counter(solution))
    #print()
    end = time.perf_counter()
    total += (end-start)
    print(solution)
    #print_board(solution)
print(str(total) + " seconds!")
