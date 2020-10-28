import sys
from collections import deque
r=sys.stdin.readline
N,M=map(int,r().split())
board=[]
for _ in range(N):
    board.append(list(map(int,r().split())))
wallcnt=0
for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            wallcnt+=1
dx=[1,-1,0,0]
dy=[0,0,1,-1]
visited=[[False]*N for _ in range(M)]
def virus(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        if 0<=x<N and 0<=y<M:
            if visited[x][y]: continue
            if board[x][y]==1: continue
            else:
                visited[x][y]=True
                for i in range(4):
                    Nx,Ny=x+dx[i],y+dy[i]
                    q.append((Nx,Ny))
def countSafe():
    total=N*M
    v=0
    wall=wallcnt+3
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                v+=1
    return total-v-wall
res=[]
for i in range(N):
    visited=[[False]*N for _ in range(M)]
    for j in range(M):
        virus(i,j)
    res.append(countSafe())
print(max(res))



