import sys
from copy import deepcopy
from collections import deque
r=sys.stdin.readline
M,N,H=map(int,r().split())
box=[]
matCnt=0
ematCnt=0
emtCnt=0
tomset=set()
for _ in range(H):
    square=[]
    for _ in range(N):
        line=list(map(int,r().split()))
        for num in line:
            if num==0:
                ematCnt+=1
            elif num==1:
                matCnt+=1
            else:
                emtCnt+=1
        square.append(line)
    box.append(square)

if ematCnt==0 or matCnt==0:
    print(0)
    exit(0)

dxyz=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def bfs():
    time=0
    q=deque()
    def ck(i,j,k):
        if not 0<=i<H:
            return False
        if not 0<=j<N:
            return False
        if not 0<=k<M:
            return False
        if box[i][j][k]!=0:
            return False
        return True
    dup=set()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k]==0:
                    tomset.add((i,j,k))
                if box[i][j][k]==1:
                    for d in range(6):
                        di,dj,dk=i+dxyz[d][0],j+dxyz[d][1],k+dxyz[d][2]
                        if (i,j,k) not in dup and ck(di,dj,dk):
                            q.append((i,j,k))
                            dup.add((i,j,k))
                            break
    flg=True
    nq=deque()
    while flg:
        if nq:
            q=nq
            nq=deque()
        flg=False
        while q:
            x,y,z=q.popleft()
            for d in range(6):
                dx,dy,dz=x+dxyz[d][0],y+dxyz[d][1],z+dxyz[d][2]
                if (dx,dy,dz) not in dup and ck(dx,dy,dz):
                    nq.append((dx,dy,dz))
                    dup.add((dx,dy,dz))
                    flg=True
        if flg:
            time+=1
    for coord in tomset:
        if coord not in dup:
            return 0
    return time

res=bfs()
if res==0:
    print(-1)
else:
    print(res)