import sys
from collections import deque
r=sys.stdin.readline
N,M=map(int,r().split())
miro=[]
for i in range(N):
    line=r().strip()
    miro.append(list(line))
    if '0' in line:
        S=(i,line.index('0'))
#abcdef 
d=[(1,0),(-1,0),(0,1),(0,-1)]
tb={
    'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,
    'a':0,'b':1,'c':2,'d':3,'e':4,'f':5
}
def bfs(x,y):
    q=deque()
    visit=[[[False]*50 for _ in range(50)] for _ in range(2**6)]
    q.append((x,y,'000000',0))
    visit[int('000000',2)][x][y]=True
    while q:
        x,y,keys,dist=q.popleft()
        for i in range(4):
            Nx,Ny=x+d[i][0],y+d[i][1]
            tmpkey=keys
            if not 0<=Nx<N or not 0<=Ny<M: continue
            cur=miro[Nx][Ny]
            if cur=='1':
                return dist+1
            if cur=='#' or visit[int(tmpkey,2)][Nx][Ny]:continue
            if cur in 'ABCDEF' and tmpkey[tb[cur]]=='0': continue
            if cur in 'abcdef':
                idx=tb[cur]
                tmpkey=tmpkey[:idx]+'1'+tmpkey[idx+1:]
            q.append((Nx,Ny,tmpkey,dist+1))
            visit[int(tmpkey,2)][Nx][Ny]=True
    return -1
print(bfs(*S))
