import sys
from collections import deque
r=sys.stdin.readline
K=int(r())
W,H=map(int,r().split())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
hx=[-2,-1,1,2,2,1,-1,-2]
hy=[1,2,2,1,-1,-2,-2,-1]
board=[]
for _ in range(H):
    board.append(list(map(int,r().split())))
if W==1 and H==1:
    print(0)
    exit(0)
visited=[[[False]*31 for _ in range(W)] for _ in range(H)]
visited[0][0]=[True]*31
def bfs(x,y):
    q=deque([(x,y,0,0)])
    while q:
        x,y,d,cnt=q.popleft()
        for j in range(8):    
            if cnt==K:
                break
            Nhx,Nhy=x+hx[j],y+hy[j]
            if 0<=Nhx<H and 0<=Nhy<W and not board[Nhx][Nhy]and not visited[Nhx][Nhy][cnt+1]:
                if Nhx==H-1 and Nhy==W-1:
                    return d+1
                visited[Nhx][Nhy][cnt+1]=True
                q.append((Nhx,Nhy,d+1,cnt+1))
        for i in range(4):
            Nx,Ny=x+dx[i],y+dy[i]
            if 0<=Nx<H and 0<=Ny<W and not board[Nx][Ny] and  not visited[Nx][Ny][cnt]:
                if Nx==H-1 and Ny==W-1:
                    return d+1
                visited[Nx][Ny][cnt]=True
                q.append((Nx,Ny,d+1,cnt))
    return -1

print(bfs(0,0))