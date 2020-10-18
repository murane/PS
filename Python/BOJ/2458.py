import sys
from collections import defaultdict
r=sys.stdin.readline
N,M=map(int,r().split())
smaller=defaultdict(set)#들어오는 노드
taller=defaultdict(set)#나가는 노드
g=[[] for _ in range(N+1)]
visited=[False]*(N+1)
for _ in range(M):
    s,t=map(int,r().split())
    g[s].append(t)
def dfs(start):
    for node in g[start]:
        visited[node]=True
        taller[start].add(node)
        taller[start].update(taller[node])
        smaller[node].add(start)
        smaller[node].update(smaller[start])
        dfs(node)
for i in range(1,N+1):
    dfs(i)
ans=0
for i in range(1,N+1):
    if len(smaller[i]|taller[i])==N-1:
        ans+=1
print(ans)


