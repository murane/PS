import sys
from collections import deque
r=sys.stdin.readline

N,M=map(int,r().split())
grid=[]
point=0
for _ in range(N):
    grid.append(list(map(int,r().split())))

# -1은 검은색 0은 무지개 1~M은 일반
# 블록 그룹은 연결된 블록의 집합이다
# 그룹에 속한 일반 블록은 모두 같은수 0은 상관없고 -1은 안됨
# 블록 그룹의 기준 블록은 일반 블록중 행, 열이 가장 작은 블록

# 1. 블록그룹 탐색, 크기, 무지개 블록수, 기준블록 행, 기준블록 열
# 2. 제거
# 3. 점수
# 4. 중력
# 5. 회전
# 6. 중력
# 7. do while 블록그룹 존재
def rotate(N):
    global grid
    tmp=[]
    for i in range(N-1,-1,-1):
        tmp.append([grid[x][i] for x in range(N)])
    grid=tmp
    return

def gravity():
    global grid
    for col in range(N):
        for row in range(N-1,-1,-1):
            if row==N-1:continue
            co,ro=col,row
            while ro<=N-2 and grid[ro][co] not in [-1,''] and grid[ro+1][co]=='':
                grid[ro][co],grid[ro+1][co]=grid[ro+1][co],grid[ro][co]
                ro+=1

def erase(coords):
    global grid
    for x,y in coords:
        grid[x][y]=''
    return

def find(x,y,visit):
    visit[x][y]=True
    q=deque([(x,y)])
    target=grid[x][y]
    save=[(x,y)]
    rainbow=[]
    while q:
        x,y=q.popleft()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny=x+dx,y+dy
            if not 0<=nx<N or not 0<=ny<N: continue
            if visit[nx][ny]:continue
            if grid[nx][ny]==0 or grid[nx][ny]==target:
                q.append((nx,ny))
                visit[nx][ny]=True
                if grid[nx][ny]==0: rainbow.append((nx,ny))
                save.append((nx,ny))
    for x,y in rainbow:
        visit[x][y]=False
    if len(save)>=2:
        return len(save),len(rainbow),save
    return -1,_,_
def getGroup(visit):
    lst=[]
    for i in range(N):
        for j in range(N):
            if grid[i][j]=='':continue
            if visit[i][j] or not 1<=grid[i][j]<=M:continue
            size,rainbow,coords=find(i,j,visit)
            if size!=-1:
                lst.append([size,rainbow,i,j,coords])
    return lst

while True:
    visit=[[False]*N for _ in range(N)]
    lst=getGroup(visit)
    lst.sort(key=lambda x: (-x[0],-x[1],-x[2],-x[3]))

    if not lst:break

    size,rainbow,i,j,coords=lst[0]
    
    erase(coords)
    point+=size**2
    gravity()
    rotate(N)
    gravity()

print(point)

