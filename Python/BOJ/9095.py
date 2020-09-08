import sys
import operator as op
from itertools import product
from functools import reduce
r=sys.stdin.readline
def nCr(n,r):
    r=min(r,n-r)
    denom=reduce(op.mul,range(n,n-r,-1),1)
    numer=reduce(op.mul,range(1,r+1),1)
    return denom//numer
def ott(num):
    arr=[]
    for i in range(num//3,-1,-1):
        for j in range((num-3*i)//2,-1,-1):
            for k in range(num-i*3-j*2,-1,-1):
                if i*3+j*2+k==num:
                    arr.append((k,j,i))
    return arr

for _ in range(int(r())):
    n=int(r())
    res=0
    for case in ott(n):
        s=sum(case)
        res+=nCr(s,case[0])*nCr(s-case[0],case[1])*nCr(s-case[0]-case[1],case[2])
    print(res)
    