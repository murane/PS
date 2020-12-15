import sys
from collections import deque
r=sys.stdin.readline
N,M=map(int,r().split())
miro=[]
for _ in range(N):
    miro.append(list(r().strip()))
di=[(1,0),(0,1),(-1,0),(0,-1)]
def bfs():
    visit=[[-1]*M for _ in range(N)]
    q=deque([(0,0)])
    visit[0][0]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+di[i][0],y+di[i][1]
            if not 0<=nx<N or not 0<=ny<M: continue
            if visit[nx][ny]!=-1: continue
            if miro[nx][ny]=='0': continue
            q.append((nx,ny))
            visit[nx][ny]=visit[x][y]+1
            if nx==N-1 and ny==M-1:
                return visit[nx][ny]+1
print(bfs())
