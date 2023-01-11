# -*- coding: utf-8 -*-
import sys
import ast

def convertToBool(n):
    s = ""
    while(n != 0 and n != 1):
        s = str((n%2)) + s
        n = int(n/2)
    s = str(n) + s
    return s
    
def truth_table(bits, n):
    size = 2**bits
    
    dicte = {}
    answer = convertToBool(n)
    while(len(answer) != size):
            answer = "0" + answer
            
    for i in range(size-1,-1,-1):
        s = convertToBool(i)
        while(len(s) != bits):
            s = "0" + s
        liste = list(s)
        tuple1 = tuple(liste)
        
        index = size-i-1
        
        dicte[tuple1] = (answer[index])
        
    return dicte

def print_pretty_tt(table):
    for key in table:
        val = table[key]
        print(key[0] + " | " + key[1] + " | " + val)

def step(num):
    if num > 0:
        return 1
    else:
        return 0

def perceptron(A, w, b, x):
    sumw = 0
    for i in range(0,len(w)):
        sumw += int(w[i])*int(x[i])
    sol = A(sumw+b)
    return sol

def check(n,w,b):
    table = (truth_table(len(w), n))
    correct = 0
    tried = 0
    for key in table:
        ans = perceptron(step, w, b, key)
        if str(ans) == table[key]:
            correct += 1
            tried += 1
        else:
            tried += 1
    print(correct/tried)

n = int(sys.argv[1])
t = ast.literal_eval(sys.argv[2])
b = float(sys.argv[3])

check(n, t, b)







