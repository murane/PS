import sys,heapq
r=sys.stdin.readline
N,M=map(int,r().split())
g=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,r().split())
    g[a].append((b,1))
    g[b].append((a,1))
INF=int(10e9)
dist=[INF]*(N+1)
dist[1]=0

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        cost,cur=heapq.heappop(q)
        if dist[cur]<cost:
            continue
        for node in g[cur]:
            if dist[node[0]]>node[1]+cost:
                dist[node[0]]=node[1]+cost
                heapq.heappush(q,(dist[node[0]],node[0]))

dijkstra(1)
lst=[]
for i in range(1,N+1):
    if not lst:
        lst.append(i)
    else:
        if dist[lst[-1]] <dist[i]:
            lst=[i]
        elif dist[lst[-1]]==dist[i]:
            lst.append(i)
lst.sort()
print(f'{lst[0]} {dist[lst[-1]]} {len(lst)}')