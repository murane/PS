import sys
from collections import deque
r=sys.stdin.readline
N,L,R=map(int,r().split())
A=list()
for _ in range(N):
    A.append(list(map(int,r().split())))
def bfs(x,y):
    q=deque([(x,y)])
    #union에 연합을 저장
    union=[(x,y)]
    ck[x][y]=1
    while q:
        x,y=q.popleft()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny=x+dx,y+dy
            if not 0<=nx<N or not 0<=ny<N:continue
            if ck[nx][ny]==1:continue
            #인접좌표가 연합이 가능하면 union에 저장하고
            #ck에 체크를 해주면서 q에 넣고 bfs를 진행
            if L<=abs(A[x][y]-A[nx][ny])<=R:
                union.append((nx,ny))
                ck[nx][ny]=1
                q.append((nx,ny))
    #1을 넘으면 첫좌표이외에 연합이 존재하므로 이동을 시킨다
    if len(union)>1:
        population=sum(map(lambda x: A[x[0]][x[1]],union)) // len(union)
        for x,y in union:
            A[x][y]=population
            #연합이 된 좌표들이 다음 이동의 후보가 되어 nextQ에 삽입된다
            nextQ.append((x,y))
        return True
    return False
#상하좌우에서 연합할 후보가 있는지 체크한다
def necessary(x,y):
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx,ny=x+dx,y+dy
        if not 0<=nx<N or not 0<=ny<N:continue
        if L<=abs(A[x][y]-A[nx][ny])<=R:
            return True
    return False
cnt=0
#모든좌표를 bfs하는대신 인구이동이될 후보만 큐에 넣어준다
nextQ=deque()
for i in range(N):
    for j in range(N):
        nextQ.append((i,j))
while True:
    flg=False
    #연합여부를 체크해주는 ck리스트
    ck=[[0]*N for _ in range(N)]
    #처음에 넣은 사이즈만큼 연합을 체크
    size=len(nextQ)
    for _ in range(size):
        i,j=nextQ.popleft()
        #연합이 안되있고 인접 좌표중에 연합할 후보가 있으면
        if ck[i][j] or not necessary(i,j):continue
        #bfs를 진행한다
        if bfs(i,j):
            flg=True
    #연합을 한적이있으면 cnt를 증가
    if flg: cnt+=1
    if not flg:
        print(cnt)
        exit(0)