import sys
import cProfile
r = sys.stdin.readline

def bertran(n):
    tb=[False,False]+[True]*(2*n-1)
    for i in range(2, int((2*n)**0.5)+1):
        if tb[i]:
            for j in range(i*2,2*n+1,i):
                tb[j]=False
    return tb

while True:
    n = int(r())
    if n==0:
        break
    else:
        print(bertran(n)[n+1:2*n+1].count(True))