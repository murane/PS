import sys
r=sys.stdin.readline
N=int(r())
g=[[] for _ in range(N+1)]
for _ in range(N):
    a,b=map(int,r().split())
    g[a].append(b)
    g[b].append(a)

visit=[0]*(N+1)
parent=[0]*(N+1)
fin=[False]*(N+1)

def dfs(cur):
    visit[cur]=True
    for nxt in g[cur]:
        if not visit[nxt]:
            parent[nxt]=cur
            dfs(nxt)
        elif not fin[nxy]:
    fin[cur]=True
        
