import sys
import heapq
from collections import defaultdict
r=sys.stdin.readline
N,E=map(int,r().split())
graph=defaultdict(set)
for _ in range(E):
    s,e,c=map(int,r().split())
    graph[s].add((e,c))
    graph[e].add((s,c))
v1,v2=map(int,r().split())
INF=sys.maxsize

def di(start:int,end:list):
    lst=[INF]*(N+1)
    heap=[]
    heapq.heappush(heap,(0,start))
    lst[start]=0
    while heap:
        dist,cur=heapq.heappop(heap)
        if lst[cur]<dist:
            continue
        for node,cost in graph[cur]:
            if lst[node]>dist+cost:
                lst[node]=dist+cost
                heapq.heappush(heap,(lst[node],node))
    return [lst[x] for x in end] 

dist1=di(v1,[1,v2,N])
dist2=di(v2,[1,v1,N])
dist1,dist2=dist1[:2]+[dist2[2]],dist2[:2]+[dist1[2]]
if INF in dist1 or INF in dist2:
    print(-1)
else:
    print(min(sum(dist1),sum(dist2)))