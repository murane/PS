import sys
from collections import deque
r=sys.stdin.readline
h,w=map(int,r().split())
pan=[]
for _ in range(h):
    pan.append(list(map(int,r().split())))

cheezes=set()
for i in range(h):
    for j in range(w):
        if pan[i][j]==1:
            cheezes.add((i,j))

def ck(lst):
    target=[]
    for x,y in lst:
        if pan[x][y]!=1:continue
        flg=False
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny=x+dx,y+dy
            if not 0<=nx<h or not 0<=ny<w: continue
            if pan[nx][ny]==0:
                flg=True
                break
        if flg:
            target.append((x,y))
    return target

def melt(lst):
    for x,y in lst:
        pan[x][y]=0
        cheezes.remove((x,y))

time=0
mem=[0]

q=deque()
q.append((0,0))
while q:
    x,y=q.popleft()
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx,ny=x+dx,y+dy
        if not 0<=nx<h or not 0<=ny<w: continue
        if pan[nx][ny]==0:

while True:
    targetLst = ck()
    if not targetLst:break

    mem.append(len(targetLst))
    time+=1
    melt(targetLst)

print(time)
print(mem[-1])