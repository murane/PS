import sys
from collections import deque
r=sys.stdin.readline
R,C=map(int,r().split())
board=[]
for _ in range(R):
    board.append(list(r().strip()))
cnt=1
dx=[1,-1,0,0]
dy=[0,0,1,-1]
record=[False]*26
record[ord(board[0][0])-65]=True
res=0
def dfs(x,y,d):
    stack=[(x,y,d)]
    global res
    res=max(res,d)
    if res==26:
        return
    for i in range(4):
        Nx,Ny=x+dx[i],y+dy[i]
        if 0<=Nx<R and 0<=Ny<C and board[Nx][Ny] and not record[ord(board[Nx][Ny])-65]:
            record[ord(board[Nx][Ny])-65]=True
            dfs(Nx,Ny,d+1)
            record[ord(board[Nx][Ny])-65]=False
dfs(0,0,1)
print(res)