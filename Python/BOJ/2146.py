import sys
from collections import deque
r=sys.stdin.readline
N=int(r())_
Map=[]
d=[(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(N):
    Map.append(list(map(int,r().split())))
def bfs(x,y,num):
    q=deque([(x,y)])
    Map[x][y]=num
    while q:
        x,y=q.popleft()
        for i in range(4):
            Nx,Ny=x+d[i][0],y+d[i][1]
            if not 0<=Nx<N or not 0<=Ny<N: continue
            if Map[Nx][Ny]!=1: continue
            Map[Nx][Ny]=num
            q.append((Nx,Ny))
cur=2
for i in range(N):
    for j in range(N):
        if Map[i][j]==1:
            bfs(i,j,cur)
            cur+=1

ans=[]
dist=sys.maxsize
for i in range(N):
    for j in range(N):
        start=Map[i][j]
<<<<<<< HEAD
        if start!=0:
            q=deque([(i,j,0)])
            while q:
                x,y,curDist=q.popleft()
                if curDist>dist or curDist>99:break
=======
        visit=[[False]*N for _ in range(N)]
        visit[i][j]=True
        if start!=0:
            q=deque([(i,j,0)])
            flg=False
            while q:
                x,y,curDist=q.popleft()
                if curDist>=dist:break
>>>>>>> 65f47ddc5ab3f8a6fd040aba753c1ca81245dc29
                for k in range(4):
                    tmpDist=curDist
                    Nx,Ny=x+d[k][0],y+d[k][1]
                    if not 0<=Nx<N or not 0<=Ny<N: continue
<<<<<<< HEAD
                    if Map[Nx][Ny]==start: continue
=======
                    if Map[Nx][Ny]==start or visit[Nx][Ny]: continue
>>>>>>> 65f47ddc5ab3f8a6fd040aba753c1ca81245dc29
                    if Map[Nx][Ny]==0:
                        tmpDist+=1
                    elif Map[Nx][Ny]!=0:
                        dist=min(dist,tmpDist)
<<<<<<< HEAD
                        break
                    q.append((Nx,Ny,tmpDist))

=======
                        flg=True
                        break
                    visit[Nx][Ny]=True
                    q.append((Nx,Ny,tmpDist))
                if flg: break
>>>>>>> 65f47ddc5ab3f8a6fd040aba753c1ca81245dc29
print(dist)
