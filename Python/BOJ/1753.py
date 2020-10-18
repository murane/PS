import sys,heapq

r=sys.stdin.readline
V,E=map(int,r().split())
K=int(r())
INF=10**9
dist=[INF]*(V+1)
g=[[] for _ in range(V+1)]
for _ in range(E):
    s,e,d=map(int,r().split())
    g[s].append((e,d))

def dijkstra(start_V):
    heap=[(0,start_V)]
    dist[start_V]=0
    heapq.heapify(heap)

    while heap:
        cost,v=heapq.heappop(heap)
        for node in g[v]:
            if dist[node[0]]>node[1]+cost:
                dist[node[0]]=node[1]+cost
                heapq.heappush(heap,(dist[node[0]],node[0]))

dijkstra(K)

for i in range(1,V+1):
    if dist[i]==INF:
        print("INF")
    else:
        print(dist[i])