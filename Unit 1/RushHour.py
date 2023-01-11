#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from collections import deque


def print_board(board):
    for r in board:
        for c in r:
            print(c, end =" ")
        print()

def check_done(board):
    row = board[2]
    x = 5
    while row[x] == "0":
        x -= 1
    if(row[x] == "X"):
        return True
    return False

def movements(string, board, car, size):
    set = {"1"}
    set.remove("1")
    horizontal = False
    r = 0
    row =0
    for row2 in board:
        row += 1
        if row2.count(str(car)) > 1:
            r = row2
            horizontal = True
            break
    start = 0
    end = 0
    if horizontal:
        for x in range(0, len(r)):
            if r[x] == str(car):
                start = x
                break
        end = start + size - 1
        spaceL = 0
        spaceR = 0
        for x in range(start-1, 0):
            if r[x] == "0":
                spaceL += 1
            else:
                break
        for y in range(end+1, 5):
            if r[y] == "0":
                spaceR += 1
            else:
                break
        temp = board.copy()
        while spaceL != 0:
            temp[row][start-1] = str(car)
            temp[row][end] = "0"
            set.add(temp)
            start -= 1
            end -= 1
            spaceL -= 1
        temp = board.copy()
        while spaceR != 0:
            temp[row][start] = "0"
            temp[row][end+1] = str(car)
            set.add(temp)
            start += 1
            end += 1
            spaceR -= 1
    else:
        column = ""
        col = 0
        start = 0
        end = 0
        spaceL = 0
        spaceR = 0
        for row in board:
            for x in range(0, len(row)):
                if x == str(car):
                    col = x
                    break
            break
        column = board[0][col] + board[1][col] + board[2][col] + board[3][col] + board[4][col] + board[5][col] 
        for c in column:
            if c == str(car):
                start = c
                break
        end = start + size - 1
        for x in range(start-1, 0):
            if column[x] == "0":
                spaceL += 1
            else:
                break
        for y in range(end+1, 5):
            if column[y] == "0":
                spaceR += 1
            else:
                break
        temp = board.copy()
        while spaceL != 0:
            temp[start-1][col] = str(car)
            temp[end][col] = "0"
            set.add(temp)
            start -= 1
            end -= 1
            spaceL -= 1
        temp = board.copy()
        while spaceR != 0:
            temp[start][col] = "0"
            temp[end+1][col] = str(car)
            set.add(temp)
            start += 1
            end += 1
            spaceR -= 1  
    return set
        

def get_children(board, string, cars):
    set = {"1"}
    set.remove("1")
    for i in range(1, cars):
        size = string.count(str(i))
        chils = movements(string, board, i, size)
        for x in chils:
            set.add(chils)
    for board in set:
        print_board(board)

s = "111002003002XX3002403055400060777060"

count = 1
board = [(s[i:i+6]) for i in range(0, len(s), 6)]

for row in range(0, 6):
    board[row] = list(board[row])

set = {"y"}
for i in range(0, 36): 
    if s[i] not in set:
        count += 1
        set.add(s[i])
count -= 2

get_children(board, s, count)
print(check_done(board))
print(count)
