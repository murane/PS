import sys
from collections import defaultdict
r=sys.stdin.readline
N,K=map(int,r().split())
chess=[]
for _ in range(N):
    chess.append(list(map(int,r().split())))

d=[(0,1),(0,-1),(-1,0),(1,0)]
horse=[]                        # i번째 체스말은 (r,c)좌표
chessStack=defaultdict(list)    # (r,c) 좌표에 있는 체스말 i,,
for i in range(K):
    r,c,d=map(int,r().split())
    horse.append([r-1,c-1,d-1])
    chessStack[(r-1,c-1)].append(i)
turn=0
def move(i):
    x,y,di=horse[i]
    nx,ny=x+d[di][0],y+d[di][1]
    if (not 0<=nx<N or not 0<=ny<N) or chess[nx][ny]==2:

    else:
        stack=chessStack[(x,y)]
        idx=stack.index(i)
        chessStack[(x,y)]=chessStack[(x,y)][:idx]
        cur=stack[stack.index(i):]
        if chess[nx][ny]==0:
            chessStack[(nx,ny)].extend(cur)
        elif chess[nx][ny]==1:
            chessStack[(nx,ny)].extend(reversed(cur))
    if len(chessStack[(nx,ny)])>=4:
        return True
    return False
while turn<1000:
    turn+=1
    flg=False
    for i in range(K):
        if move(i):
            flg=True
            break
    if flg:
        break
print(turn if turn>1000 else -1)