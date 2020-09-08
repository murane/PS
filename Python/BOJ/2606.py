import sys
r=sys.stdin.readline
N=int(r())
graph=[[0]]+[[] for _ in range(N)]
for _ in range(int(r())):
    a,b=map(int,r().split())
    graph[a].append(b)
    graph[b].append(a)
for lst in graph:
    lst.sort()
def dfs(start_v):
    visited=[]
    stack=[start_v]
    while stack:
        v=stack.pop()
        if v not in visited:
            visited.append(v)
            stack.extend(graph[v])
    return visited
print(len(dfs(1))-1)