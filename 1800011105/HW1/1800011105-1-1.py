#!/usr/bin/env python
# coding=utf-8

epsilon_M=1e-6

print("(1) Expand directly:")

def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i

    return fac

for x in range(0,110,10):
    n = 0
    e_minusx = 0
    an = 0
    while True:
        an = (-1*x)**n/factorial(n)
        e_minusx = e_minusx + an
        if (abs(an/e_minusx) < epsilon_M/2):
            break
        n = n + 1
    print("e^{-%d}=%g"%(x,e_minusx))
print("")


print("(2) Recursion:")

for x in range(0,110,10):
    n = 0
    e_minusx = 0
    sn = 1
    while True:
        e_minusx += sn
        sn = -sn*x/(n+1)
        if (abs(sn/e_minusx) < epsilon_M/2):
            break
        n = n + 1
    print("e^{-%d}=%g"%(x,e_minusx))
print("")


print("(3) Reciprocal:")
for x in range(0,110,10):
    n = 0
    e_x = 0
    sn = 1
    while True:
        e_x = e_x + sn
        sn = sn*x/(n+1)
        if (abs(sn/e_x) < epsilon_M/2):
            break
        n = n + 1
    e_minusx=1/e_x 
    print("e^{-%d}=%g"%(x,e_minusx))
