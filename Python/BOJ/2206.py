import sys
from collections import deque
r=sys.stdin.readline
N,M=map(int,r().split())
d=[(1,0),(-1,0),(0,1),(0,-1)]
Map=[]
for _ in  range(N):
    Map.append(list(r().strip()))
visited=[[[False,False] for _ in range(M)] for _ in range(N)]
visited[0][0]=[1,1]
def bfs():
    q=deque([(0,0,True)])
    while q:
        x,y,flg=q.popleft()
        if visited[N-1][M-1][0]!=False or visited[N-1][M-1][1]!=False:
            print(max(visited[N-1][M-1]))
            exit(0)
        for i in range(4):
            Nx,Ny=x+d[i][0],y+d[i][1]
            if 0<=Nx<N and 0<=Ny<M:
                if Map[Nx][Ny]=='0':#벽x
                    if flg and not visited[Nx][Ny][0]:#벽x
                        visited[Nx][Ny][0]=visited[x][y][0]+1
                        q.append((Nx,Ny,True))
                    elif not visited[Nx][Ny][1]:#벽O
                        visited[Nx][Ny][1]=visited[x][y][1]+1
                        q.append((Nx,Ny,False))
                else:#벽
                    if flg and not visited[Nx][Ny][1]:#벽x
                        visited[Nx][Ny][1]=visited[x][y][0]+1
                        q.append((Nx,Ny,False))
                    else:#벽O
                        continue

bfs()
print(-1)