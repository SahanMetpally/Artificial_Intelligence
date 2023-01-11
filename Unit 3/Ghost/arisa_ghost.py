# -*- coding: utf-8 -*-

import sys

s = sys.argv[1]
ml = int(sys.argv[2])
words_list = set()  
# alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
game = ""
# player = "odd"
dic_children = dict()

if len(sys.argv) > 3:
    game = sys.argv[3].upper()
    # if len(game)%2 != 0:
    #     player = "even"

with open(s) as f:
    for line in f:
        line = line.strip().upper()
        if len(line) >= ml and line.isalpha() and line[:len(game)] == game:
            words_list.add(line)


def create_dict():
    # global words_list, alpha, dic_children
    # for w in words_list:
    #     for i in range(1, len(w)):
    #         temp = w[:i]
    #         if temp not in words_list:
    #             if temp not in dic_children:
    #                 dic_children[temp] = set()
    #                 dic_children[temp].add(w)
    #             else:
    #                 dic_children[temp].add(w)
    global words_list, dic_children
    for w in words_list:
        for i in range(1, len(w)):
            temp = w[:i]
            if temp not in dic_children.keys():
                dic_children[temp] = set()
                dic_children[temp].add(w[:i+1])
            else:
                dic_children[temp].add(w[:i+1])
            
def next_word(word):
    # moves = []
    # for a in alpha:
    #     temp = word + a
    #     if temp not in words_list:
    #         for w in words_list:
    #             if temp in w:
    #                 moves.append((temp, a))
    #                 break;
    # return moves
    moves = []
    if word in dic_children:
        future_words = dic_children[word]
        for w in future_words:
            # moves.append((w[:len(word)+1], w[len(word)]))
            moves.append((w, w[len(word)]))
    return moves

def game_over(word):
    if word in words_list:
        return True
    return False

# def score(word):
#     if len(word)%2 == 0:
#         if player == "even":
#             return -1
#         else:
#             return 1
#     else:
#         if player == "even":
#             return 1
#         else:
#             return -1
        

def max_step(word, alpha, beta): # return max weight of future outcome
    # print(word)
    # input()
    if word in words_list:
        # print(word + " " + score)
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
    # print(word)
    # input()
    if word in words_list:
        # print(word + " " + score)
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
        if res == 1:
            values.append(m)
    return values 


# =============================================================================
# RUN CODE
# =============================================================================
create_dict()
wins = max_move(game, float('-inf'), float('inf'))
if len(wins) == 0:
    print("Next player will lose!")
else:
    print("Next player can guarantee victory by playing any of these letters: %s" % wins)