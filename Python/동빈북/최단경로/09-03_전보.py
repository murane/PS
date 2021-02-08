import sys,heapq
from collections import defaultdict
r=sys.stdin.readline
N,M,C=map(int,r().split())
g=[[] for _ in range(N+1)]
INF=int(10e9)
dist=[INF]*(N+1)
for _ in range(M):
    start,end,cost=map(int,r().split())
    g[start].append((end,cost))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    dist[start]=0
    while q:
        cost,cur=heapq.heappop(q)
        if dist[cur]<cost:
            continue
        for node in g[cur]:
            if dist[node[0]]>node[1]+cost:
                dist[node[0]]=node[1]+cost
                heapq.heappush(q,(dist[node[0]],node[0]))
dijkstra(C)
cnt=len([x for x in dist if x!=INF and x!=0])
ans=max([x for x in dist if x!=INF])
print(f'{cnt} {ans}')