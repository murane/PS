import sys
from collections import deque
r=sys.stdin.readline
M,N=map(int,r().split())
miro=[]
INF=sys.maxsize
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for _ in range(N):
    miro.append(list(map(int,list(r().strip()))))

visited=[[[False,INF] for _ in range(M)] for _ in range(N)]
visited[0][0]=[True,0]
def bfs(x,y):
    q=deque([(x,y,0)])
    while q:
        x,y,cnt=q.popleft()
        for i in range(4):
            Nx,Ny=x+dx[i],y+dy[i]
            if 0<=Nx<N and 0<=Ny<M:#범위안에 들어오면
                if visited[Nx][Ny][0]==False:
                    if miro[Nx][Ny]==0:
                        q.appendleft((Nx,Ny,cnt))
                        visited[Nx][Ny]=[True,cnt]
                    else:
                        q.append((Nx,Ny,cnt+1))
                        visited[Nx][Ny]=[True,cnt+1]
                else:
                    if miro[Nx][Ny]==0 and visited[Nx][Ny][1]>cnt:
                        q.appendleft((Nx,Ny,cnt))
                        visited[Nx][Ny][1]=cnt
                    elif miro[Nx][Ny]==1 and visited[Nx][Ny][1]>cnt+1:
                        q.append((Nx,Ny,cnt+1))
                        visited[Nx][Ny][1]=cnt+1

bfs(0,0)
print(visited[N-1][M-1][1])

