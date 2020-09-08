import sys
r=sys.stdin.readline
N,M=map(int,r().split())
graph=[[] for _ in range(N+1)]
check=[0]*(N+1)
for _ in range(M):
    u,v=map(int,r().split())
    graph[u].append(v)
    graph[v].append(u)
def dfs(start_v):
    visited=[]
    stack=[start_v]
    while stack:
        v=stack.pop()
        if v not in visited:
            visited.append(v)
            check[v]=1
            for w in graph[v]:
                stack.append(w)
cc=0
for i in range(1,N+1):
    if check[i]!=1:
        dfs(i)
        cc+=1
print(cc)