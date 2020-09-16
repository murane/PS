import sys
from collections import deque
r=sys.stdin.readline
N,M=map(int,r().split())
coins=[]
board=[list(r().strip()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j]=="o":
            board[i][j]=="."
            coins.append((i,j))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def button(c1,c2,d,cnt):
    flg1,flg2=False,False
    a=(c1[0]+dx[d],c1[1]+dy[d])
    b=(c2[0]+dx[d],c2[1]+dy[d])
    if (a[0]<0 or a[0]>=N) or (a[1]<0 or a[1]>=M):#떨어짐
        flg1=True
    if (b[0]<0 or b[0]>=N) or (b[1]<0 or b[1]>=M):#떨어짐
        flg2=True
    if flg1^flg2:
        print(cnt)
        exit(0)
    if flg1 and flg2:
        return
    if board[a[0]][a[1]]=="#":#벽일때
        a=c1
    if board[b[0]][b[1]]=="#":#벽일때
        b=c2
    if board[a[0]][a[1]]=="#" and board[b[0]][b[1]]=="#":#둘다 벽이라 안움직임
        return
    if a==b:#겹침
        return
    return (a,b)
#초기좌표에서 상하좌우
q=deque()
q.append((1,coins[0],coins[1]))
while q:
    cur = q.popleft()
    if cur[0]==11:
        continue
    for d in range(4):
        res = button(cur[1],cur[2],d,cur[0])
        if res:
            q.append((cur[0]+1,res[0],res[1]))
    #초기좌표에서 상하좌우로 움직임을 수행함
    #움직일수 없다? or 움직이면 둘다 떨어진다? or 11번째이다? 버림
    #버튼누른횟수를 증가시키고 4방향버튼누르는 경우를 append한다
print("-1")