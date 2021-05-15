import sys
from functools import reduce
r=sys.stdin.readline
N,M=map(int,r().split())
g=[[] for _ in range(N+1)]
visit=[False]*(N+1)
for _ in range(M):
    A,B=map(int,r().split())
    A,B=A-1,B-1
    g[A].append(B)
    g[B].append(A)

def dfs(v,arr):
    visit[v]=True
    s.append(v)
    for nxt in g[v]:
        if not visit[nxt]:
            visit(nxt,s)
ans=1
for i in range(N):
    if not visit[i]:
        s=[]
        visit(i,s)