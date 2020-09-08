import sys
from collections import defaultdict

def recur_dfs(v, visited=[]):
    visited.append(v)
    for w in graph[v]:
        if not w in visited:
            visited = recur_dfs(w,visited)
    return visited
def iter_dfs(start_v):
    visited=[]
    stack=[start_v]
    while stack:
        v=stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited
def bfs(start_v):
    visited=[start_v]
    queue=[start_v]
    while queue:
        v=queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited

r=sys.stdin.readline
N,M,V=list(map(int,r().split()))
graph=defaultdict(list)
for _ in range(M):
    a,b=map(int,r().split())
    graph[b].append(a)
    graph[a].append(b)
for lst in graph:
    graph[lst].sort()

print(' '.join(map(str,recur_dfs(V))))
print(' '.join(map(str,bfs(V))))