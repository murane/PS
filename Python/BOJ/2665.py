import sys
from collections import deque
r=sys.stdin.readline
n=int(r())
room=[]
for _ in range(n):
    room.append(list(r().strip()))
di=[(1,0),(0,1),(-1,0),(0,-1)]
visit=[[-1]*n for _ in range(n)]
def bfs():
    q=deque()
    q.append((0,0))
    visit[0][0]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+di[i][0],y+di[i][1]
            if not 0<=nx<n or not 0<=ny<n: continue 
            if visit[nx][ny]==-1:
                if room[nx][ny]=='0':
                    visit[nx][ny]=visit[x][y]+1
                    q.append((nx,ny))
                else:
                    visit[nx][ny]=visit[x][y]
                    q.appendleft((nx,ny))
bfs()
print(visit[n-1][n-1])