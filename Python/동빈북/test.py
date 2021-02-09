import sys
from collections import deque
from copy import deepcopy
r=sys.stdin.readline
N=int(r())
board,q=[],deque()
ans=0
for _ in range(N):
    board.append(list(map(int,r().split())))
def dfs(N):
    global ans,board
    if N==5:
        ans=max(ans,max(map(max,board)))
        return
    tmpBoard=deepcopy(board)
    for i in range(4):
        move(i)
        dfs(N+1)
        board=deepcopy(tmpBoard)
def get(i,j):
    if board[i][j]:
        q.append(board[i][j])
        board[i][j]=0
def merge(i,j,di,dj):
    while q:
        cur=q.popleft()
        if not board[i][j]:
            board[i][j]=cur
        elif board[i][j]==cur:
            board[i][j]=cur*2
            i,j=i+di,j+dj
        else:
            i,j=i+di,j+dj
            board[i][j]=cur
def move(k):
    if k == 0:
        for j in range(N):
            for i in range(N):
                get(i, j)
            merge(0, j, 1, 0)
    elif k == 1:
        for j in range(N):
            for i in range(N-1, -1, -1):
                get(i, j)
            merge(N-1, j, -1, 0)
    elif k == 2:
        for i in range(N):
            for j in range(N):
                get(i, j)
            merge(i, 0, 0, 1)
    else:
        for i in range(N):
            for j in range(N-1, -1, -1):
                get(i, j)
            merge(i, N-1, 0, -1)
dfs(0)   
print(ans)
