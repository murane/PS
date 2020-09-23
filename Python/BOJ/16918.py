import sys
from copy import deepcopy
r=sys.stdin.readline
R,C,N=map(int,r().split())
board=[list(r().strip()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j]=="O":
            board[i][j]=1
        else:
            board[i][j]=-1
def printBoard():
    for i in range(R):
        for j in range(C):
            if board[i][j]==-1:
                print(".",end="")
            else:
                print("O",end="")
        print("")
def boom(coords):
    for x,y in coords:
        for x,y in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
            if 0<=x<R and 0<=y<C:
                board[x][y]=-1
def setboom(tmp):
    for i in range(R):
        for j in range(C):
            if board[i][j]==-1:
                board[i][j]=0
            else:
                board[i][j]+=1
                if board[i][j]==3:
                    board[i][j]=-1
                    tmp.append((i,j))
    return tmp
if N==1:
    pass
else:
    time=1
    while True:
        tmp=setboom([])
        boom(tmp)
        time+=1
        if time==N:
            break
printBoard()