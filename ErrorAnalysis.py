# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:06:18 2020

@author: skyle
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def sine(x,N): 
    term = x
    sinx = x
    for i in range(2,N):
        term = -term*x*x/((2*i-1)*(2*i-2)) 
        sinx = sinx + term
    return sinx
x = float(input("Enter an angle in degrees: "))
N = int(input("Enter the number of steps: "))  
if x > 360:
    x = x% 360
x *= math.pi/180

logDiff = np.zeros(1000) # Array with 1000 elements
logN = np.zeros(1000) # Array with 1000 elements
n = 1
for n in range(2,1000):
    if abs(sine(x, n) - sine(x, 2*n)) == 0:
        break
    logDiff[n-1] = math.log10(abs(sine(x, n) - sine(x, 2*n)))
    logN[n-1] = math.log10(n)
    n += 1

for n in range (2, n):
    print (logN[n-1], logDiff[n-1])
plt.xlabel("logN")
plt.ylabel("logDiff")

plt.plot(logN,logDiff, "o")
plt.show()
print (sine(x,N))
print(math.sin(x))