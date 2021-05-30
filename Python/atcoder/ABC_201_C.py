import sys,math
r=sys.stdin.readline
S=r().strip()
O=S.count('o')
Q=S.count('?')
import operator as op
from functools import reduce

def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

def nPr(n,r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, 1, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

if O>4:
    print(0)
else:
    select=nCr(4,O)
    