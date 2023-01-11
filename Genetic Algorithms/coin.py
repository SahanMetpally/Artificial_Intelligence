# -*- coding: utf-8 -*-

import random


uiuc = 0
ucsd = 0 

for i in range(0,100):
    temp = random.uniform(0, 1)
    if temp <= 0.5:
        uiuc+= 1
    else:
        ucsd += 1

print("UIUC " + str(uiuc))
print("UCSD " + str(ucsd))