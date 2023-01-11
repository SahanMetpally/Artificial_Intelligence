#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


#Euler 11
print("Euler 11:")

board = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48".split(" ")
matrix = [[0 for x in range(20)] for y in range(20)] 
maxi = 0

for i in range(0,20):
    for j in range(0,20):
        matrix[i][j] = board[20*i+j]

for i in range(0,20):
    for j in range(0,17):
        val = int(matrix[i][j])*int(matrix[i][j+1])*int(matrix[i][j+2])*int(matrix[i][j+3])
        if  val > maxi:
            maxi = val
        val = int(matrix[j][i])*int(matrix[j+1][i])*int(matrix[j+2][i])*int(matrix[j+3][i])
        if val > maxi:
            maxi = val
for i in range(0,17):
    for j in range(0,17):
        val = int(matrix[i][j])*int(matrix[i+1][j+1])*int(matrix[i+2][j+2])*int(matrix[i+3][j+3])
        if val > maxi:
            maxi = val
        val = int(matrix[16-i][19-j])*int(matrix[17-i][18-j])*int(matrix[18-i][17-j])*int(matrix[19-i][16-j])
        if val > maxi:
            maxi = val

print(maxi)
print()

#Euler 12
print("Euler 12")

sett = set()
settL = set()

def is_prime(x):
    if(x in sett):
        return True
    elif(x in settL):
        return False
    prime = True
    y = int(x**0.5)
    if(x ==1):
        settL.add(x)
        return False
    if(x != 2):
        if(x%2 == 0):
            settL.add(x)
            return False
    for i in range(3, y+1):
        if(x%i == 0):
            settL.add(x)
            return False
        i += 1
    if(prime):
        sett.add(x)
    else:
        settL.add(x)
    return prime

x = 12000
while True:
    triangle = (x*(x+1))/2
    divisors = 1
    count = 0
    for i in range(2,int(triangle/2)):
        if(is_prime(i)):
            while(triangle%i == 0):
                triangle = triangle/i
                count += 1
        divisors = divisors * (count + 1)
        if triangle == 1:
            break
        count = 0  
        
    if(divisors > 499):
        print(int((x*(x+1))/2))
        break
    x += 1
    
print()
#Euler 14
print("Euler 14")
maxCount = 0
maxStart = 0

for l in range(800000, 1000000):
    count = 1
    temp= l
    while temp != 1:
        if(temp%2 == 0):
            temp = temp/2
        else:
            temp = 3*temp + 1
        count += 1
    if(count > maxCount):
        maxCount = count
        maxStart = l
print(maxStart)
print()

#Euler 21
print("Euler 21")
dicte = {}
def sumOfFactors(n):
    if n not in dicte:
        summ = 0
        for i in range(1, int(n/2)+1):
            if(n%i == 0):
                summ += i
        dicte[n] = summ
        return summ
    else:
        return dicte[n]
count = 0
for i in range(1, 10000):
    if(sumOfFactors(sumOfFactors(i)) == i and sumOfFactors(i) != i):
        count += i
print(count)
print()

#Euler 24
print("Euler 24")
from itertools import permutations

permutations = list(permutations("0123456789"))
print("".join(permutations[999999]))
print()

#Euler 30
print("Euler 30")

count = 0
for i in range(2,531441):
    string = str(i)
    tot = 0
    for j in string:
        tot += int(j)**5
    if i == tot:
        count += i
print(count)
