import sys
from collections import deque
r=sys.stdin.readline
H,W=map(int,r().split())
grid=[]
for _ in range(H):
    grid.append(list(r().strip()))
teleportor=[[] for _ in range(26)]
S=(0,0)
for i in range(H):
    for j in range(W):
        ch=grid[i][j]
        if ch.islower():
            teleportor[ord(ch)-97].append((i,j))
        elif ch=='S':
            S=(i,j)
visit=[[-1]*W for _ in range(H)]
di=[(1,0),(-1,0),(0,1),(0,-1)]
def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit[x][y]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            Nx,Ny=x+di[i][0],y+di[i][1]
            if not 0<=Nx<H or not 0<=Ny<W: continue
            cur=grid[Nx][Ny]
            if cur=="#" or visit[Nx][Ny]!=-1: continue
            if cur=='G':
                return visit[x][y]+1
            visit[Nx][Ny]=visit[x][y]+1
            q.append((Nx,Ny))

        if grid[x][y].islower():
            for nx,ny in teleportor[ord(grid[x][y])-97]:
                if visit[nx][ny]==-1:
                    visit[nx][ny]=visit[x][y]+1
                    q.append((nx,ny))
            teleportor[ord(grid[x][y])-97].clear()
    return -1

print(bfs(*S))