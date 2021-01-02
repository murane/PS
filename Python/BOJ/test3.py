import sys
from collections import defaultdict
r=sys.stdin.readline
N,Q=map(int,r().split())
query=[]
g=defaultdict(list)
for i in range(1,N+1):
    a,b=map(int,r().split())
    g[a].append(b)
    g[b].append(a)
for _ in range(Q):
    u,v=map(int,r().split())
    query.append([u,v])
for u,v in query:
