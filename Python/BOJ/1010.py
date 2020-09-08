import sys
from functools import reduce
import operator as op
r=sys.stdin.readline
def nCr(n,r):
    r=min(r, n-r)
    numerator=reduce(op.mul, range(n,n-r,-1), 1)
    denominator = reduce(op.mul, range(1,r+1),1)
    return numerator//denominator
for _ in range(int(r())):
    N,M=map(int,r().split())
    print(nCr(M,N))
