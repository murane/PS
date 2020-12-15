import sys
from collections import deque
r=sys.stdin.readline
N=int(r())
zido=[]
for _ in range(N):
    zido.append(list(map(int,r().strip())))
di=[(1,0),(0,1),(-1,0),(0,-1)]
num=2
lst=[]
def bfs(x,y,num):
    q=deque()
    q.append((x,y))
    zido[x][y]=num
    cnt=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+di[i][0],y+di[i][1]
            if not 0<=nx<N or not 0<=ny<N: continue
            if zido[nx][ny]!=1: continue
            cnt+=1
            zido[nx][ny]=num
            q.append([nx,ny])
    return cnt
for i in range(N):
    for j in range(N):
        if zido[i][j]==1:
            lst.append(bfs(i,j,num))
            num+=1
print(len(lst))
lst.sort()
for cnt in lst:
    print(cnt)
