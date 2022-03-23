#!/usr/bin/env python
# coding=utf-8
from numpy import log
from numpy import exp

for n in range(1,11):
    lnHn=0
    Hn=0
    for i in range(1,2*n):
        if(i<n):
            an = (2*n - 3*i)*log(i)
        else:
            an = -(2*n - i)*log(i)
        
        lnHn = lnHn + an
        Hn = exp(lnHn)
    print("det(H_%d) = %g"%(n,Hn))
