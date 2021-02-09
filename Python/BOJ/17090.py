import sys
from collections import deque,defaultdict
r=sys.stdin.readline
N,M=map(int,r().split())
miro=[]
for _ in range(N):
    miro.append(list(r().strip()))
tb={'U':(-1,0),'R':(0,1),'D':(1,0),'L':(0,-1)}
parent=dict()
sys.setrecursionlimit(10**9)
for i in range(N):
    for j in range(M):
        parent[(i,j)]=(i,j)
def find(x):
    if parent[x]==x:
        return x
    parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    X=find(x)
    Y=find(y)
    if X==Y:
        return
    parent[X]=Y
visit=[[False]*M for _ in range(N)]
ck=defaultdict(bool)
def ckCycle(i,j):
    q=deque([(i,j)])
    visit[i][j]=True
    flg=False
    while q:
        x,y=q.popleft()
        nx,ny=x+tb[miro[x][y]][0],y+tb[miro[x][y]][1]
        #미로안
        if 0<=nx<N and 0<=ny<M:
            #방문했을경우
            if visit[nx][ny]:
                #밖으로 나가게되었다!
                if find((nx,ny)) in ck and ck[find((nx,ny))]:
                    union((x,y),(nx,ny))
                    flg=True
                else:#사이클이다!
                    union((x,y),(nx,ny))
                    ck[find((x,y))]=False
            #처음방문
            else:
                union((x,y),(nx,ny))
                visit[nx][ny]=True
                q.append((nx,ny))
        #밖으로 나가는좌표의 경우...
        else:
            ck[find((i,j))]=True
            flg=True
    return flg
cnt=0
for i in range(N):
    for j in range(M):
        if visit[i][j]:
            if ck[find((i,j))]:
                cnt+=1
            continue
        else:
            if ckCycle(i,j):
                cnt+=1
print(cnt)