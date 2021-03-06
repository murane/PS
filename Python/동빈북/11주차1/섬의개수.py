import sys
from collections import deque
r=sys.stdin.readline
while True:
    w,h=map(int,r().split())
    if w==0 and h==0:
        break
    sea=[]
    for _ in range(h):
        sea.append(list(map(int,r().split())))
    v=[[False]*w for _ in range(h)]
    ans=0

    def bfs(x,y):
        q=deque([(x,y)])
        v[x][y]=True
        while q:
            x,y=q.popleft()
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                nx,ny=x+dx,y+dy
                if not 0<=nx<h or not 0<=ny<w: continue
                if v[nx][ny]: continue
                if sea[nx][ny]==0: continue
                q.append((nx,ny))
                v[nx][ny]=True


    #가로w 세로h
    for i in range(h):
        for j in range(w):
            if not v[i][j] and sea[i][j]==1:
                bfs(i,j)
                ans+=1
    print(ans)

    