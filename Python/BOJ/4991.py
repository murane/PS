import sys
from collections import deque
r=sys.stdin.readline
def bfs(x,y):
    q=deque()
    q.append((x,y,'0'*len(dirty),0))
    visit=[[[False]*w for _ in range(h)] for _ in range(2**len(dirty))]
    visit[int('0'*len(dirty),2)][x][y]=True
    while q:
        x,y,mask,dist=q.popleft()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny=x+dx,y+dy
            tmpDist=dist
            tmpMask=mask
            if not 0<=nx<h or not 0<=ny<w: continue
            if bang[nx][ny]=='X': continue
            tmpDist+=1
            if visit[int(tmpMask,2)][nx][ny]: continue
            if bang[nx][ny]=='.':
                q.append((nx,ny,tmpMask,tmpDist))
                visit[int(tmpMask,2)][nx][ny]=True
            elif bang[nx][ny]=='*':
                idx=dirty[(nx,ny)]
                tmpMask=tmpMask[:idx]+'1'+tmpMask[idx+1:]
                visit[int(tmpMask,2)][nx][ny]=True
                q.append((nx,ny,tmpMask,tmpDist))
                if tmpMask=='1'*len(dirty):
                    return tmpDist
    return -1
while True:
    w,h=map(int,r().split())
    if w==h==0:break
    bang=[]
    for i in range(h):
        bang.append(list(r().strip()))
    dirty={}
    seq=-1
    start=[]
    for i in range(h):
        for j in range(w):
            if bang[i][j]=='o':
                start=[i,j]
                bang[i][j]='.'
            elif bang[i][j]=='*':
                seq+=1
                dirty[(i,j)]=seq
    print(bfs(start[0],start[1]))
    