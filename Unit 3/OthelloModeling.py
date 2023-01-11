#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

puzzle = sys.argv[1]
player = sys.argv[2]

w, h = 8, 8;
board = [[0 for x in range(w)] for y in range(h)] 

for i in range(0,8):
    for j in range(0,8):
        board[i][j] = puzzle[8*i + j]
        
        
        
def valid(board, player, opponent, i, j, x, y):
    #print(board)
    #print(str(i) + " " + str(j) + " " +str(x) + " " + str(y))
    if board[i+x][j+y] != opponent:
        return False
    t = board[i+x][j+y]
    i += x
    j += y
    while t != player and i >= 0 and i < 8 and j >= 0 and j < 8 and t != ".":
        t = board[i][j]
        i += x
        j += y
    if t == player:
        return True
    return False

def possibleMoves(board, player):
    got = False
    liste = []
    if player == "x":
        opponent = "o"
    else:
        opponent = "x"
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j] != opponent and board[i][j] != player:
                for x in range(-1,2):
                    for y in range(-1,2):
                        if i+x >= 0 and i+x< 8 and j+y >= 0 and j+y<8:
                            if not (x == 0 and y == 0):
                                if valid(board, player, opponent, i, j, x, y):
                                    liste.append(i*8 + j)
                                    got = True
                                    break
                    if got:
                        got = False
                        break
    return liste

def moveBoard(board, player, opponent, move):
    t = [x[:] for x in board]
    for x in range(-1,2):
        for y in range(-1,2):
            row = int(move/8)
            col = move%8
            t[row][col] = player
            if row+x >= 0 and row+x< 8 and col+y >= 0 and col+y<8:
                if not (x == 0 and y == 0):
                    if valid(board, player, opponent, row, col, x, y):
                        checker = board[row+x][col+y]
                        row += x
                        col += y
                        while checker != player and row >= 0 and row < 8 and col >= 0 and col < 8:
                            checker = board[row][col]
                            t[row][col] = player
                            row += x
                            col += y
    temp = [''.join(x) for x in t] 
    print("".join(temp))

moves = possibleMoves(board, player)
if player == "x":
    opponent = "o"
else:
    opponent = "x"
print(moves)
for move in moves:
    moveBoard(board, player, opponent, move)