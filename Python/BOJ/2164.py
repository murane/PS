import sys
from collections import deque
r=sys.stdin.readline
N=int(r())
DQ=deque([x for x in range(1,N+1)])
while True:
    if len(DQ)==1:
        print(DQ[0])
        break
    DQ.popleft()
    DQ.append(DQ[0])
    DQ.popleft()