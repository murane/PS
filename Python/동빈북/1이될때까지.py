import sys
from collections import deque
r=sys.stdin.buffer.readline
N,K=map(int,r().split())
tb=[-1]*(10**6+1)
tb[N]=0
def bfs(n):
    q=deque()
    q.append(n)
    while q:
        x=q.popleft()
        if x%K==0:
            q.append(x//K)
            tb[x//K]=tb[x]+1
        q.append(x-1)
        tb[x-1]=tb[x]+1
        if tb[1]!=-1:
            print(tb[1])
            exit(0)
bfs(N)