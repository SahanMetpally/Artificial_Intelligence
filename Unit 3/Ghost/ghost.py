# -*- coding: utf-8 -*-
import math
import sys

filename = sys.argv[1]
min_length = int(sys.argv[2])
curr_game = ""

if(len(sys.argv) == 4):
    curr_game = sys.argv[3].upper()

file = open(filename)
dictWords = []
build = {}

for line in file:
    line = line.strip()
    line = line.upper()
    if(line.isalpha() and len(line)>= min_length) and len(curr_game) < len(line):
        valid = True
        for i in range(0,len(curr_game)):
            if line[i] != curr_game[i]:
                valid = False
        if valid:
            dictWords.append(line.upper()[len(curr_game):])
            line = line[len(curr_game):]
            for i in range(1, len(line)):
                t = line[0:i]
                if t in build.keys():
                    build[t].add(line[0:i+1])
                else:
                    build[t] = set()
                    build[t].add(line[0:i+1])
        
temp = "Q W E R T Y U I O P A S D F G H J K L Z X C V B N M".split(" ")
letters = set(temp)
usable = set(temp)

for l in usable:
    v = False
    for w in dictWords:
        if w[0] == l:
            v = True
            break
    if not v:
        temp.remove(l)
        
letters = set(temp)
answer = []

def get_words(start):
    building = build[start]
    return building

def max_step(word,alpha,beta):
    if word in dictWords:
        return 1
    results = []
    poss = get_words(word)
    for s in poss:
        res = min_step(s,alpha,beta)
        if res > alpha:
            alpha = res
        if alpha >= beta:
            return alpha
        results.append(res)
    return max(results)
    
def mid_step(word,alpha,beta):
    if word in dictWords:
        return 0
    results = []
    poss = get_words(word)
    for s in poss:
        res = max_step(s,alpha,beta)
        if res < beta:
            beta = res
        if beta <= alpha:
            return beta
        results.append(res)
    return min(results)
    
def min_step(word,alpha,beta):
    if word in dictWords:
        return -1
    results = []
    poss = get_words(word)
    for s in poss:
        res = mid_step(s,alpha,beta)
        if res < beta:
            beta = res
        if beta <= alpha:
            return beta
        results.append(res)
    return min(results)
    
for l in letters:
    if min_step(l, -math.inf, math.inf) == 1:
        answer.append("'"+l+"'")
answer.sort()
if len(answer) >= 0:
    print("Next player will lose!")
else:
    print("Next player can guarantee victory by playing any of these letters: [" + ", ".join(answer) + "]")
