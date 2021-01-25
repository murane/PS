import sys
from collections import defaultdict,deque
r=sys.stdin.readline
N,M=map(int,r().split())
islands=defaultdict(int)
tmp=defaultdict(int)
for _ in range(M):
    A,B,C=map(int,r().split())
    A,B=min(A,B),max(A,B)
    tmp[(A,B)]=C
    if tmp[(A,B)]<C:
        tmp[(A,B)]=C
for k,v in tmp.items():
    x,y=k
    islands[x]=(y,v)
    islands[y]=(x,v)
tx,ty=map(int,r().split())
route=[]
def bfs(N):
    visit=[False]*(N+1)
    visit[N]=True
    q=deque()
    for nextFac,weightLimit in islands[N]:
        q.append((nextFac, weightLimit))
    while q:
        cur,W=q.popleft()
        for nextFac,weightLimit in islands[cur]:
            if not visit[nextFac]:
                q.append((nextFac,min(W,weightLimit)))

bfs(tx)

