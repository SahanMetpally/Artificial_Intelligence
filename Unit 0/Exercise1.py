#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

sum = 0;
index = 2;
fib = 0;

def Fib(n):
    if n<=0:
        print("Please retry with a number greater than 0")
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)

if sys.argv[1] == "A":
    print(int(sys.argv[2]) + int(sys.argv[3]) + int(sys.argv[4]))

elif sys.argv[1] == "B":
    while index < len(sys.argv):
        sum += int(sys.argv[index])
        index += 1
    print(sum)

elif sys.argv[1] == "C":
    while index < len(sys.argv):
        if int(sys.argv[index])%3 == 0:
            print(sys.argv[index])
        index += 1
        
elif sys.argv[1] == "D":
    fib = int(sys.argv[2])
    num = 1;
    while num <= fib:
        print(Fib(num))
        num += 1

elif sys.argv[1] == "E":
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    while a <= b:
        print(a*a - 3*a +2)
        a += 1

elif sys.argv[1] == "F":
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    c = float(sys.argv[4])
    if (a+b > c) and (b+c > a) and (a+c > b):
        p = (a+b+c)/2;
        print((p*(p-a)*(p-b)*(p-c))**0.5)
    else:
        print("Invalid Input: Triangle not possible")
        
elif sys.argv[1] == "G":
    word = sys.argv[2].lower()
    print("a: " + str(word.count("a")))
    print("e: " + str(word.count("e")))
    print("i: " + str(word.count("i")))
    print("o: " + str(word.count("o")))
    print("u: " + str(word.count("u")))

else:
    print("Please enter volid input")