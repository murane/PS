import sys
from collections import deque
r=sys.stdin.readline

n,k=map(int,r().split())

ck=[False]*(n+1)
g=[set() for _ in range(n+1)]
c=0
for _ in range(k):
    a,b=map(int,r().split())
    g[a].add(b)
    g[b].add(a)  

def dfs(start):
    global c
    if ck[start]:
        return
    ck[start]=True
    q=[start]
    q=deque(q)
    c+=1
    while q:
        cur = q.popleft()
        for nxt in g[cur]:
            if not ck[i]:
                q.append(i)
                ck[i]=True

for i in range(1,n+1):
    dfs(i)
print(k-(n-c))
