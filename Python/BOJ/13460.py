import sys
from collections import deque
r=sys.stdin.readline
N,M=map(int,r().split())
board=[]
D=[(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(N):
    board.append(list(r().strip()))
for i in range(N):
    for j in range(M):
        if board[i][j]=="R":
            R=[i,j]
            board[i][j]="."
        elif board[i][j]=="B":
            B=[i,j]
            board[i][j]="."

def move(x,y,d):
    dist=0
    while True:
        nextPos=board[x+d[0]][y+d[1]]
        if nextPos=='.':
            x,y=x+d[0],y+d[1]
        elif nextPos=='O':
            return True,0,[-1,-1]
        elif nextPos=='#':
            return False,dist,[x,y]
        dist+=1

def bfs():
    q=deque()
    q.append([R,B,0])
    visit=set()
    visit.add((tuple(R),tuple(B)))
    while q:
        red,blue,cnt=q.popleft()
        tmpRed,tmpBlue=red,blue
        #if cnt==10: return -1
        for i in range(4):          #4방향
            flgR,distR,red=move(tmpRed[0],tmpRed[1],D[i])#일단 움직이고보자
            flgB,distB,blue=move(tmpBlue[0],tmpBlue[1],D[i])
            if flgR and not flgB: 
                return cnt+1#빨간색은 들어가고 파란색은 아니면 성공
            elif flgB: continue             #파란색이 들어가면 실패
            elif not flgR and not flgB:     #일단 둘다 구멍에 안들어가고
                if red==blue:               #겹치는 경우
                    if distR>distB:
                        red=red[0]-D[i][0],red[1]-D[i][1]
                    else:
                        blue=blue[0]-D[i][0],blue[1]-D[i][1]
                if (tuple(red),tuple(blue)) not in visit:
                    q.append([red,blue,cnt+1])  #다시 큐로
                    visit.add((tuple(red),tuple(blue)))
    return -1
print(bfs())
