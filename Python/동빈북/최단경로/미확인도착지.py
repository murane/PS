import sys
r=sys.stdin.readline
for _ in range(int(r())):
    n,m,t=map(int,r().split())
    #정점, 간선, 목적지 후보의 갯수
    s,g,h=map(int,r().split())
    #출발지, g,h사이의 간선을 지나감....
    road=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d=map(int,r().split())
        road[a].append((b,d))
        road[b].append((a,d))
    candidate=[]
    for _ in range(t):
        candidate.append(int(r()))
    
    

