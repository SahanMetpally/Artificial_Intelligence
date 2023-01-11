# -*- coding: utf-8 -*-

import sys

s = sys.argv[1]
ml = int(sys.argv[2])
words_list = set()  
game = ""
dic_children = dict()

if len(sys.argv) > 3:
    game = sys.argv[3].upper()

with open(s) as f:
    for line in f:
        line = line.strip().upper()
        if len(line) >= ml and line.isalpha() and line[:len(game)] == game:
            words_list.add(line)


def create_dict():
    global words_list, dic_children
    for w in words_list:
        for i in range(len(w)):
            temp = w[:i]
            if temp not in words_list:
                if temp not in dic_children:
                    dic_children[temp] = set()
                    dic_children[temp].add(w[:i+1])
                else:
                    dic_children[temp].add(w[:i+1])
            
def next_word(word):
    moves = []
    if word in dic_children:
        future_words = dic_children[word]
        for w in future_words:
            moves.append((w, w[len(word)]))
    return moves

def game_over(word):
    if len(next_word(word)) == 0:
        return True
    return False


def max_step(word, alpha, beta): # return max weight of future outcome
    if word in words_list:
        return 1
    results = []
    for next_w, m in next_word(word):
        ms = min_step(next_w, alpha, beta)
        results.append(ms)
        if ms > alpha: 
            alpha = ms
        if alpha >= beta:
            break;
    return max(results)

def min_step(word, alpha, beta): # return max weight of future outcome
    if word in words_list:
        return -1
    results = []
    for next_w, m in next_word(word):
        ms = max_step(next_w, alpha, beta)
        results.append(ms)
        if ms < beta: 
            beta = ms
        if alpha >= beta:
            break;
    return min(results)

def max_move(word, alpha, beta): # return max move location, play X 
    values = []
    for next_w, m in next_word(word):
        res = min_step(next_w, alpha, beta)
        values.append((m, res))
    possible_wins = set()
    for move, val in values:
        if val == 1:
            possible_wins.add(move)
    return possible_wins   
        
# =============================================================================
# RUN CODE
# =============================================================================
create_dict()
wins = max_move(game, float('-inf'), float('inf'))
if len(wins) == 0:
    print("Next player will lose!")
else:
    print("Next player can guarantee victory by playing any of these letters: %s" % wins)