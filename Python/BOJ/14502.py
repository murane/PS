import sys
from collections import deque
from itertools import combinations
r=sys.stdin.readline
N,M=map(int,r().split())
lab,coords=[],[]
d=[(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(N):
    lab.append(list(map(int,r().split())))
res,cntOne,cntTwo=0,0,0
for i in range(N):
    for j in range(M):
        if lab[i][j]==0:
            coords.append((i,j))
        elif lab[i][j]==1:
            cntOne+=1
        elif lab[i][j]==2:
            cntTwo+=1
def bfs(lab):
    q=deque([])
    visitied=[[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if lab[i][j]==2:
                q.append((i,j))
                visitied[i][j]=True
    while q:
        x,y=q.popleft()
        for i in range(4):
            Nx,Ny=x+d[i][0],y+d[i][1]
            if 0<=Nx<N and 0<=Ny<M and lab[Nx][Ny]==0 and not visitied[Nx][Ny]:
                visitied[Nx][Ny]=True
                q.append((Nx,Ny))
    cnt=0
    for line in visitied:
        cnt+=line.count(False)
    return cnt-cntOne-3
for pick in combinations(coords,3):
    a,b,c=pick
    lab[a[0]][a[1]]=1
    lab[b[0]][b[1]]=1
    lab[c[0]][c[1]]=1
    res=max(res,bfs(lab))
    lab[a[0]][a[1]]=0
    lab[b[0]][b[1]]=0
    lab[c[0]][c[1]]=0
print(res)

