#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


constraints = []

for i in range(0, 3):
    sett = []
    for j in range(0, 3):
        sett.append(i*3 + j)
    constraints.append(sett)
for i in range(0, 3):
    sett = []
    for j in range(0, 3):
        sett.append(i + 3*j)
    constraints.append(sett)
constraints.append([0,4,8])
constraints.append([2,4,6])


def done(board):
    for checks in constraints:
        if board[checks[0]] == board[checks[1]] == board[checks[2]]:
            if board[checks[0]] == "O":
                return -1
            elif board[checks[0]] == "X":
                return 1
    if "." not in board:
        return 0
    return None

def get_moves(board, sign):
    sett = set()
    for b in range(0, 9):
        if board[b] == ".":
            sett.add(b)
    possibles = set()     
    for x in sett:
        possibles.add(board[0:x] + sign + board[x+1:])
    return possibles

def get_dots(board):
    i = 0
    for s in board:
        if s == ".":
            i += 1
    return i

def max_step(board):
    finish = done(board)
    if finish is not None:
        return finish
    results = []
    boards = get_moves(board, "X")
    for s in boards:
        results.append(min_step(s))
    return max(results)

def min_step(board):
    finish = done(board)
    if finish is not None:
        return finish
    results = []
    boards = get_moves(board, "O")
    for s in boards:
        results.append(max_step(s)) 
    return min(results)

def get_steps(board, sign):
    sett = set()
    for b in range(0, 9):
        if board[b] == ".":
            sett.add(b)
    possibles = {} 
    for x in sett:
        possibles[x] = (board[0:x] + sign + board[x+1:])
    return possibles


def print_board(state):
    print()
    print("Current board:")
    print(state[0:3] + "    012")
    print(state[3:6] + "    345")
    print(state[6:9] + "    678")
    print()

state = sys.argv[1]
cpu = "O"
empty = {0,1,2,3,4,5,6,7,8}
for i in range(0,9):
    if state[i] != ".":
        empty.discard(i)
if "X" not in state:
    cpu = input("Should I be X or O?")
else:
    countX = 0
    countO = 0
    for s in state:
        if s == "X":
            countX += 1
        elif s == "O":
            countO += 1
    if countX == countO:
        cpu = "X"
    else:
        cpu = "O"

if cpu == "X":
    print_board(state)
    while done(state) is None:
        moves = get_steps(state, cpu)
        move = 0
        for m in moves:
            move = m
            break
        result = -1
        for s in moves:
            res = min_step(moves[s])
            ans = "loss"
            if res == 1:
                ans = "win"
            elif res == 0:
                ans = "tie"
            if res > result:
                move = s
                result = res
            print("Moving at " + str(s) + " results in a " + str(ans))
        print()
        print("I choose space " + str(move))
        state = state[0:move] + "X" + state[move+1:]
        empty.discard(move)
        print_board(state)
        if done(state) is None:
            temp = ""
            for s in empty:
                temp += str(s) + ", "
            temp = temp[0:len(temp)-2] + "."
            print("You can move to any of these spaces: " + temp)
            uMove = int(input("Your Choice?"))
            state = state[0:uMove] + "O" + state[uMove+1:]
            empty.discard(uMove)
            print_board(state)

    game = done(state)
    if game == 1:
        print("I win!")
    elif game == 0:
        print("We tied!")
    else:
        print("You win!")
        
elif cpu == "O":
    print_board(state)
    if "X" not in state:
        print("You can move to any of these spaces: 0, 1, 2, 3, 4, 5, 6, 7, 8.")
        uMove = int(input("Your Choice?"))
        state = state[0:uMove] + "X" + state[uMove+1:]
        empty.discard(uMove)
        print_board(state)
    while done(state) is None:
        moves = get_steps(state, cpu)
        move = 0
        for m in moves:
            move = m
            break
        result = 1
        for s in range(0,9):
            if s in moves:
                res = max_step(moves[s])
                ans = "win"
                if res == 1:
                    ans = "loss"
                elif res == 0:
                    ans = "tie"
                if res < result:
                    move = s
                    result = res
                print("Moving at " + str(s) + " results in a " + str(ans))
        print()
        print("I choose space " + str(move))
        state = state[0:move] + "O" + state[move+1:]
        empty.discard(move)
        print_board(state)
        if done(state) is None:
            temp = ""
            for s in empty:
                temp += str(s) + ", "
            temp = temp[0:len(temp)-2] + "."
            print("You can move to any of these spaces: " + temp)
            uMove = int(input("Your Choice?"))
            state = state[0:uMove] + "X" + state[uMove+1:]
            empty.discard(uMove)
            print_board(state)

    game = done(state)
    if game == 1:
        print("You win!")
    elif game == 0:
        print("We tied!")
    else:
        print("I win!")


















