# -*- coding: utf-8 -*-

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
    return(correct/tried)

def train(bits, conical):
    possible = 2**2**bits
    correct = 0
    for i in range(conical, conical+1):
        table = truth_table(bits, i)
        
        w = []
        b = 0
        ws = []
        bs = 10
        
        for h in range(0, bits):
            w.append(0)
            ws.append(100)
        l = 1
        count = 0

        while(count < 100):
            for key in table:
                p = int(perceptron(step, w, b, key))
                if p != int(table[key]):
                    for j in range(0,bits):
                        w[j] = w[j] + (int(table[key]) - p)*int(key[j])
                    b = b + (int(table[key]) - p)
            works = True
            for s in range(0, bits):
                if w[s] != ws[s]:
                    works = False
                    break
            if b != bs:
                works = False
            if works:
                break
            else:
                ws = w.copy()
                bs = b
            count += 1
        if(int(check(i, w, b)) == 1):
            correct += 1         

    print("Final Weight Vector: " + str(w))
    print("Final Bias Value: " + str(b))
    print(check(conical, w, b))


bits = int(sys.argv[1])
conical = int(sys.argv[2])
train(bits, conical)