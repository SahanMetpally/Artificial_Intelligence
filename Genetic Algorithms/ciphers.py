# -*- coding: utf-8 -*-

from math import log
import random
import sys


cipher = "XRPHIWGSONFQDZEYVJKMATUCLB"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dictWords = {}


def encode(cipher, string):
    build = ""
    for s in string:
        s = s.upper()
        if s.isalpha():
            build += cipher[alphabet.find(s)]
        else:
            build += s
    return build

def decode(cipher, string):
    build = ""
    for s in string:
        s = s.upper()
        if s.isalpha():
            build += alphabet[cipher.find(s)]
        else:
            build += s
    return build

def read(filename):
    file = open(filename)

    for line in file:
        s = line.split(" ")[0]
        x = line.split(" ")[1]
        dictWords[s] = x

def fitness(n, encoded, cipher):
    ngrams = set()
    score = 0.0
    for i in range(0,len(encoded)-n):
        temp = encoded[i:i+n]
        word = True
        for t in temp:
            if not t.isalpha():
                word = False
                break
        if word:
            w = decode(cipher, temp)
            ngrams.add(w)
            if w in dictWords:
                score += log(int(dictWords[w]),2)
    return score

def hill_climb(encoded, cipher):
    sent = decode(cipher, encoded)
    score = fitness(4,sent, cipher)
    temp = cipher
    while True:
        ran1 = random.randint(0, 25)
        ran2 = random.randint(0, 25)
        strlst = list(temp)
        strlst[ran1], strlst[ran2] = strlst[ran2], strlst[ran1]
        temp = "".join(strlst)
        sent = decode(temp, encoded)
        score2 = fitness(4, sent, temp)
        if score2 > score:
            score = score2
            print(sent)
            print()
    
read("ngrams.txt")

#encoded = "ZFNNANWJWYBZLKEHBZTNSKDDGJWYLWSBFNSSJWYFNKBGLKOCNKSJEBDWZFNGKLJKJNQFJPFJBXHBZTNRDKNZFNPDEJWYDRPDEGCNZNWJYFZZFLZTCNBBNBZFNNLKZFSLKONWBLCCKJANKBPHGBZFNGNLOBLWSRDCSBZFNRJWLCBFDKNJWLWSWDTDSUWDTDSUOWDQBQFLZBYDJWYZDFLGGNWZDLWUTDSUTNBJSNBZFNRDKCDKWKLYBDRYKDQJWYDCSJZFJWODRSNLWEDKJLKZUJNANWZFJWODRDCSSNLWEDKJLKZUZFNRLZFNKQNWNANKRDHWSJZFJWODRSNLWEDKJLKZU"
encoded = sys.argv[1]

population = {}
pop = []

POPSIZE = 500
CLONES = 1
TOURNSIZE = 20
WINP = 0.75
CROSS = 5
MUTATE = 0.7

bestS = 0
bestC = "A"

while len(population) < POPSIZE:
    al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0,100):
        ran1 = random.randint(0, 25)
        ran2 = random.randint(0, 25)
        strlst = list(al)
        strlst[ran1], strlst[ran2] = strlst[ran2], strlst[ran1]
        al = "".join(strlst)
    if al not in population:
        sc = fitness(3, encoded, al)
        if sc > bestS:
            bestS = sc
            bestC = al
        population[al] = sc
        pop.append(al)


def combine(one, two):
    sizes = []
    for x in range(0,26):
        sizes.append(x)
    indexes = random.sample(sizes, CROSS)
    newString = ".........................."
    newWord = list(newString)
    for x in indexes:
        newWord[x] = one[x]
    for x in two:
        if x not in newWord:
            for y in range(0,26):
                if newWord[y] == ".":
                    newWord[y] = x
                    break
    newString = "".join(newWord)
    
    if random.random() > MUTATE:
        ran1 = random.randint(0, 25)
        ran2 = random.randint(0, 25)
        strlst = list(newString)
        strlst[ran1], strlst[ran2] = strlst[ran2], strlst[ran1]
        newString = "".join(strlst)
    return newString

def breed(parents):
    things = random.sample(parents, TOURNSIZE*2)
    tourn1 = things[:TOURNSIZE]
    tourn2 = things[TOURNSIZE:]
    
    maxS1 = 0
    maxC1 = 0
    maxS2 = 0
    maxC2 = 0
    for i in range(0, TOURNSIZE):
        if population[tourn1[i]] > maxS1:
            maxS1 = population[tourn1[i]]
            maxC1 = tourn1[i]
        if population[tourn2[i]] > maxS2:
            maxS2 = population[tourn2[i]]
            maxC2 = tourn2[i]

    if random.random() < WINP:
        answer = combine(maxC1, maxC2)
    else:
        maxS12 = 0
        maxC12 = 0
        maxS22 = 0
        maxC22 = 0
        while True:
            for i in range(0, TOURNSIZE):
                if population[tourn1[i]] > maxS12 and population[tourn1[i]] < maxS1:
                    maxS12 = population[tourn1[i]]
                    maxC12 = tourn1[i]
                if population[tourn2[i]] < maxS2 and population[tourn2[i]] > maxS22:
                    maxS22 = population[tourn2[i]]
                    maxC22 = tourn2[i]
            if random.random() < WINP:
                break
        answer = combine(maxC12, maxC22)
    return answer

for i in range(0,300):
    #print(i)
    newPopulation = {}
    newPop = []
    newPopulation[bestC] = bestS
    newPop.append(bestC)
    while len(newPopulation) <  POPSIZE:
        t = breed(pop)
        s = fitness(3, encoded, t)
        if t not in newPopulation:
            newPopulation[t] = s
            newPop.append(t)
    bestS = 0
    bestC = "A"
    for s in newPop:
        if newPopulation[s] > bestS:
            bestC = s
            bestS = newPopulation[s]
    print("Cipher: " + bestC + " Score: " + str(bestS))
    print(decode(bestC, encoded))
    print()
    population = newPopulation.copy()
    pop = newPop.copy()

#print(bestC)
print(decode(bestC, encoded))












