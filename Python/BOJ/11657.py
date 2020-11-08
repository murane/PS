import sys
from collections import defaultdict
r=sys.stdin.readline
N,M=map(int,r().split())
city=defaultdict(set)
for _ in range(M):
    S,E,C=map(int,r().split())
    city[S].add((E,C))
INF=sys.maxsize
dist=[INF]*(N+1)
dist[1]=0
flg=False
for i in range(N):
    for _from in range(1,N+1):
        for to,cost in city[_from]:
            if dist[_from]!=INF and dist[to]>dist[_from]+cost:
                dist[to]=dist[_from]+cost
                if i==N-1: flg=True
for i in range(len(dist)):
    if dist[i]==INF:
        dist[i]=-1
if flg:
    print(-1)
else:
    print('\n'.join(list(map(str,dist[2:]))))