import sys
from collections import deque
r=sys.stdin.readline
def delonepan(lod,ch):
    while True:
        if lod and lod[0]==ch:
            lod=lod[1:]
        else:
            break
    return lod
A=r().split()
if len(A)>1:
    A=A[1]
    delonepan(A,'A')
else:
    A=''
B=r().split()
if len(B)>1:
    B=B[1]
    delonepan(B,'B')
else:
    B=''
C=r().split()
if len(C)>1:
    C=C[1]
    delonepan(C,'C')
else:
    C=''
