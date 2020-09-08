import sys
from collections import deque
r=sys.stdin.readline
N,K=map(int,r().split())
Q=deque(range(1,N+1))
res=[]
while Q:
    Q.rotate(-(K-1))
    res.append(Q[0])
    Q.popleft()
tmp=', '.join(map(str,res))
print(f'<{tmp}>')