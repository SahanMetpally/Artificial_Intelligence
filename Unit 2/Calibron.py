#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time

puzzle = sys.argv[1].split()
puzzle_height = int(puzzle[0])
puzzle_width = int(puzzle[1])
rectangles = [(int(temp.split("x")[0]), int(temp.split("x")[1])) for temp in puzzle[2:]]

solved = {}
area = 0
for x in rectangles:
    area += x[0]*x[1]

def get_next_unassigned(state):
    return state.find(".")

def get_sorted_values(recta):
    rec = [((int(x[1])), int(x[0])) for x in recta]
    poss = rec + recta
    return poss
def print_board(state):
    for i in range(0, puzzle_height):
        for j in range(0+i*puzzle_width, 0+i*puzzle_width + puzzle_width):
             print(state[j], end = " ")
        print()
    print()
def csp_backtracking(state, recta, solved):
    #print_board(state)
    #time.sleep(0.25)
    if "." not in state:
        return solved
    var = get_next_unassigned(state)
    t = recta
    for val in t:
        r = recta.copy()
        r.remove(val)
        r.remove((val[1], val[0]))
        height = val[0]
        width = val[1]
        fit = True
        if width <= puzzle_width-var%puzzle_width and height <= puzzle_height - int(var/puzzle_width):
            for i in range(0,height):
                for j in range(0, width):
                    if state[var + j + puzzle_width*i] != ".":
                        fit = False
        if width <= puzzle_width-var%puzzle_width and height <= puzzle_height - int(var/puzzle_width) and fit:
            s = list(state)
            for i in range(0,height):
                for j in range(0, width):
                    s[var + j + puzzle_width*i] = "a"
            
            sol = solved.copy()
            sol[var] = (val)
            temp = "".join(s)
            result = csp_backtracking(temp, r, sol)
            if result is not None:
                return result
    return None
    
    
if area != puzzle_height*puzzle_width:
    print("Containing rectangle incorrectly sized.")
    
else:
    start = time.perf_counter()

    solution = csp_backtracking("."*puzzle_height*puzzle_width, get_sorted_values(rectangles), solved)
    
    end = time.perf_counter()

    if solution == None:
        print("No Solution.")
    else:
        for line in solution:
            row = int(line/puzzle_width)
            column = int(line%puzzle_width)
            height = solution[line][0]
            width = solution[line][1]
            print(str(row) + " " + str(column) + " " + str(height) + " " + str(width))
    print(str(end-start) + " seconds!")
            
            

