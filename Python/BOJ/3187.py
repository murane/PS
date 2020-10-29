import sys
from collections import deque
r=sys.stdin.readline
R,C=map(int,r().split())
field=[]
for _ in range(R):
    field.append(list(r().strip()))
visit=[[0]*C for _ in range(R)]
d=[(1,0),(-1,0),(0,1),(0,-1)]
def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit[x][y]=1
    s,w=0,0
    if field[x][y]=='v':w+=1
    elif field[x][y]=='k':s+=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            Nx,Ny=x+d[i][0],y+d[i][1]
            if not 0<=Nx<R or not 0<=Ny<C: continue
            if visit[Nx][Ny] or field[Nx][Ny]=='#': continue
            if field[Nx][Ny]=='v':
                w+=1
                #print(f'wolf on {Nx} {Ny}')
            elif field[Nx][Ny]=='k':
                s+=1
                #print(f'sheep on {Nx} {Ny}')
            q.append((Nx,Ny))
            visit[Nx][Ny]=1
    return (s,0) if s>w else (0,w)

S,W=0,0
for i in range(R):
    for j in range(C):
        if field[i][j]=='#': continue
        if not visit[i][j]:
            s,w=bfs(i,j)
            #print(f'{i},{j}>{s},{w}')
            S+=s
            W+=w
print(S,W)