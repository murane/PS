import sys,heapq
r=sys.stdin.readline
INF=int(1e9)
n,m=map(int,r().split())
start=int(r())

graph=[[] for i in range(n+1)]

dist=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,r().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    dist[start]=0
    while q:
        d,now=heapq.heappop(q)
        if dist[now]<d:
            continue
        for i in graph[now]:
            cost=d+i[1]
            if cost<dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

