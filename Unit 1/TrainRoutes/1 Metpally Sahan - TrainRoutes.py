#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import pi , acos , sin , cos
import sys
import time
from collections import deque
from heapq import heappush, heappop, heapify

def calcd(lat1, long1, lat2, long2):
   y1 = lat1 
   x1 = long1
   y2 = lat2 
   x2 = long2
   #all assumed to be in decimal degrees
   #y1, x1 = node1
   #y2, x2 = node2

   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

start = time.perf_counter()

filename = "rrNodes.txt"
file = open(filename)
dicte = {}
for line in file:
    loc = line.split(" ")[0]
    lon = line.split(" ")[1]
    lat = line.split(" ")[2]
    lat = lat[0:len(lat)-1]
    tuple1 = (lon, lat)
    dicte[loc] = tuple1
    
filename = "rrEdges.txt"
file = open(filename)
dicte2 = {}
for line in file:
    one = line.split(" ")[0]
    two = line.split(" ")[1]
    two = two[0:len(two)-1]
    lat1 = float(dicte[one][0])
    lon1 = float(dicte[one][1])
    lat2 = float(dicte[two][0])
    lon2 = float(dicte[two][1])
    dist = calcd(lat1, lon1, lat2, lon2)
    sett = set()
    tuple1 = (two, dist)
    tuple2 = (one, dist)
    if not one in dicte2.keys():
        sett.add(tuple1)
        dicte2[one] = sett
    else:
        dicte2[one].add(tuple1)
    sett = set()
    if not two in dicte2.keys():
        sett.add(tuple2)
        dicte2[two] = sett
    else:
        dicte2[two].add(tuple2)

filename = "rrNodeCity.txt"
file = open(filename)
dicteLoc = {}
for line in file:
    pos = line.index(" ")
    name = line[pos+1:].strip()
    loc = line[0:pos]
    dicteLoc[name] = loc
    
end = time.perf_counter()

print("Time to create data structure: " + str(end-start))
    
def get_children(node):
    return dicte2[node]

def djikstra(string, goal):
    setT = set()
    depth = 0.0
    tuple = (depth, string)
    heap_list = []
    heappush(heap_list, tuple)
    while heap_list:
        tuple2 = heappop(heap_list)
        if(tuple2[1] == goal):
            return tuple2[0]
        temp = tuple2[1]
        if temp not in setT:
            setT.add(temp)
            answers = get_children(temp)
            for children in answers:
                if children[0] not in setT:
                    dist = tuple2[0] + children[1]
                    tuple3 = (dist, children[0])
                    heappush(heap_list, tuple3)
    return None

def a_star(string, goal):
    lat1 = float(dicte[goal][0])
    lon1 = float(dicte[goal][1])
    lat2 = float(dicte[string][0])
    lon2 = float(dicte[string][1])
    setT = set()
    depth = 0.0
    dist = calcd(lat1, lon1, lat2, lon2)
    tuple = (dist+depth, depth, string)
    heap_list = []
    heappush(heap_list, tuple)
    while heap_list:
        tuple2 = heappop(heap_list)
        if(tuple2[2] == goal):
            return tuple2[1]
        temp = tuple2[2]
        if temp not in setT:
            setT.add(temp)
            answers = get_children(temp)
            for children in answers:
                if children[0] not in setT:
                    depth = tuple2[1] + children[1]
                    lat2 = float(dicte[children[0]][0])
                    lon2 = float(dicte[children[0]][1])
                    dist = calcd(lat1, lon1, lat2, lon2)
                    tuple3 = (dist+depth, depth, children[0])
                    heappush(heap_list, tuple3)
    return None

#print(dicte2)
first = "Austin"#sys.argv[1]
last = "Atlanta"#sys.argv[2]

start = time.perf_counter()
length = (djikstra(dicteLoc[first],dicteLoc[last]))
end = time.perf_counter()
print(first + " to " + last + " with Dijkstra: " + str(length) + " in " + str(end-start) + " seconds.")

start = time.perf_counter()
length = (a_star(dicteLoc[first],dicteLoc[last]))
end = time.perf_counter()
print(first + " to " + last + " with A*: " + str(length) + " in " + str(end-start) + " seconds.")















