import sys
from heapq import heappop,heappush
r=sys.stdin.readline
N=int(r())
space=[list(map(int,r().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if space[i][j]==9:
            curPos=(i,j)
            space[i][j]=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    curSize=2
    curFeedCnt=0
    curTime=0
    visited=[[False]*N for _ in range(N)]
    q=[]
    heappush(q,(0,x,y))
    while q:
        d,x,y=heappop(q)
        if 0<space[x][y]<curSize:
            curFeedCnt+=1
            space[x][y]=0
            if curFeedCnt==curSize:
                curSize+=1
                curFeedCnt=0
            curTime+=d
            d=0
            q.clear()
            visited=[[False]*N for _ in range(N)]
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<N and space[nx][ny]<=curSize and not visited[nx][ny]:
                visited[nx][ny]=True
                heappush(q,(d+1,nx,ny))
    print(curTime)
bfs(curPos[0],curPos[1])