import sys
r=sys.stdin.readline
sys.setrecursionlimit(10**9)
N=int(r())
g=[[] for _ in range(N+1)]
for _ in range(N):
    a,b=map(int,r().split())
    g[a].append(b)
    g[b].append(a)

visit=[0]*(N+1)
parent=[0]*(N+1)
fin=[False]*(N+1)
cycle=set()

def dfs(cur):
    visit[cur]=True
    if fin[cur]:
        return
    for nxt in g[cur]:
        if not visit[nxt]:
            parent[nxt]=cur
            dfs(nxt)
        elif not fin[nxt] and parent[cur]!=nxt:
            tmpCur,tmpNxt=cur,nxt
            cycle.add(cur)
            while tmpCur!=tmpNxt:
                tmpCur=parent[tmpCur]
                cycle.add(tmpCur)
    fin[cur]=True

dfs(1)
ans=[0]*(N+1)

def dist(start):
    visit = [-1]*(N+1)
    visit[start]=0
    stack=[start]
    while stack:
        cur=stack.pop()
        for nxt in g[cur]:
            if visit[nxt]!=-1:
                continue
            else:
                stack.append(nxt)
                visit[nxt]=visit[cur]+1
                if cur in cycle:
                    ans[start]=visit[nxt]-1
                    return

for i in range(1,N+1):
    if i in cycle:
        continue
    else:
        dist(i)

print(*ans[1:])