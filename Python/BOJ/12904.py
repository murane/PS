import sys
from collections import Counter
r=sys.stdin.readline
S=r().strip()
T=r().strip()

while len(T)!=len(S):
    if T[-1]=='A':
        T=T[0:-1]
    else:
        T=T[0:-1]
        T=T[::-1]
if S==T:
    print(1)
else:
    print(0)
