#!/usr/bin/env python
# coding=utf-8

print("GEM:")
def GEM(H,b):
    n=len(b)
    for index in range(0, n):
    ## i means the row in matrix (begening at 1) while index means the index in array (begening at 0)
    ## So I write 'index' in complete for distinguishment and also 'jndex'
        temp = H[index][index]
        if temp == 0:
            break
            print("ERROR!!!")

        for jndex in range(index, n):
            H[index][jndex] *= 1/temp
        b[index] *= 1/temp
        ## normalized the row of H[index] and b[index]

        for index1 in range(index+1, n):
            if index1 == index:
                continue
            temp1 = H[index1][index]
            k=H[index1][index]/H[index][index]

            for jndex1 in range(index, n):
                H[index1][jndex1] -= H[index][jndex1]*k
            b[index1] -= b[index]*k

    return H,b
    ## having transformed H into an upper triangle matrix

def back_substitution(H,b):
    x=[0 for i in range(len(b))]

    for index in range(n-1,-1,-1):
        if H[index][index]==0:
            print("ERROR!!!")
        x[index]=b[index]

        for jndex in range(n-1, index, -1):
            x[index] -= H[index][jndex]*x[jndex]
        x[index]/=H[index][index]

    return x


for n in range(1,11):
    H=[[2/(i+j-1) for i in range(1,n+1)] for j in range(1,n+1)]
    b=[1 for i in range(1, n+1)]
    H,b=GEM(H,b)
    x=back_substitution(H,b)


    for i in range(n):
        x[i]=round(x[i],2)

    print("When n=%d, the solution x is"%n)
    print(x)
    print("")


print("\n")
print("Cholesky:")

from numpy import sqrt

def Cholesky(A):
    n=len(A)
    H=[[0 for i in range(n)] for j in range(n)]
    for jndex in range(0,n):
        for kndex in range(0,jndex,1):
            A[jndex][jndex] -= A[jndex][kndex]**2

        A[jndex][jndex]=sqrt(A[jndex][jndex])
        H[jndex][jndex]=A[jndex][jndex]

        for index in range(jndex+1, n):
            for kndex in range(0,jndex,1):
                A[index][jndex] -= A[index][kndex]*A[jndex][kndex]

            A[index][jndex] /= A[jndex][jndex]
            H[jndex][index]=A[index][jndex]

    return H
    ## H is upper left triangle matrix, and A=H^{\dagger}H

def back_substitution(H,b):
    x=[0 for i in range(len(b))]

    for index in range(n-1,-1,-1):
        if H[index][index]==0:
            print("ERROR!!!")
        x[index]=b[index]

        for jndex in range(n-1, index, -1):
            x[index] -= H[index][jndex]*x[jndex]
        x[index]/=H[index][index]

    return x

def forward_substitution(H,b):
    x=[0 for i in range(len(b))]

    for index in range(0,n):
        if H[index][index]==0:
            print("ERROR!!!")
        x[index]=b[index]

        for jndex in range(0,index):
            x[index] -= H[index][jndex]*x[jndex]

        x[index]/=H[index][index]

    return x

for n in range(1,11):
    H=[[2/(i+j-1) for i in range(1,n+1)] for j in range(1,n+1)]
    b=[1 for i in range(1, n+1)]
    H=Cholesky(H)
    H_dagger=[[H[j][i] for j in range(n)] for i in range(n)]
    y=forward_substitution(H_dagger,b)
    x=back_substitution(H,y)
    for i in range(n):
        x[i]=round(x[i],2)

    print("When n=%d, the solution x is"%n)
    print(x)
    print("\n")
