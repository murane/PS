import sys
from collections import defaultdict
r=sys.stdin.readline
N,K=map(int,r().split())
chess=[]
for _ in range(N):
    chess.append(list(map(int,r().split())))

dxy=[(0,1),(0,-1),(-1,0),(1,0)]
tb={
    0:1,1:0,2:3,3:2
}
horse=[]                        # i번째 체스말은 (r,c)좌표
chessStack=defaultdict(list)    # (r,c) 좌표에 있는 체스말 i,,
for i in range(K):
    row,col,d=map(int,r().split())
    horse.append([row-1,col-1,d-1])
    chessStack[(row-1,col-1)].append(i)
def move(i,flg):
    x,y,di=horse[i]
    if flg:
        di=tb[di]
        horse[i][2]=di
    nx,ny=x+dxy[di][0],y+dxy[di][1]
    if (not 0<=nx<N or not 0<=ny<N) or chess[nx][ny]==2:
        if not flg:
            return move(i,True)
        else:
            return False
    else:
        idx=chessStack[(x,y)].index(i)
        cur=chessStack[(x,y)][idx:]
        chessStack[(x,y)]=chessStack[(x,y)][:idx]
        for j in cur:
            horse[j]=[nx,ny,horse[j][2]]
        if chess[nx][ny]==0:
            chessStack[(nx,ny)].extend(cur)
        elif chess[nx][ny]==1:
            chessStack[(nx,ny)].extend(reversed(cur))
    if len(chessStack[(nx,ny)])>=4:
        return True
    return False
turn=0
while turn<=1000:
    turn+=1
    flg=False
    for i in range(K):
        if move(i,False):
            flg=True
            break
    if flg:
        break
print(turn if turn<=1000 else -1)