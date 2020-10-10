import sys
from copy import deepcopy
from collections import deque
r=sys.stdin.readline
N,L,R=map(int,r().split())
A=[list(map(int,r().split())) for _ in range(N)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
#모든나라를 스캔함
#연합이 존재하는지 체크함
#연합이 없으면 인구 이동 횟수를 출력
#연합이 있으면 각 연합별로 인구 이동을 시행
def bfs(x,y):
    visited=set([(x,y)])
    q=deque([(x,y)])
    union=set()
    s=0
    while q:
        x,y=q.popleft()
        union.add((x,y))
        s+=A[x][y]
        for i in range(4):
            Nx,Ny=x+dx[i],y+dy[i]
            if 0<=Nx<N and 0<=Ny<N:
                if (Nx,Ny) in visited:continue
                if check[Nx][Ny]:continue
                if L<=abs(A[x][y]-A[Nx][Ny])<=R:
                    q.append((Nx,Ny))
                    visited.add((Nx,Ny))
    return union,int(s/len(union))

cnt=0
while True:
    flg=False
    check=[[0]*N for _ in range(N)]     
    #city=deepcopy(A)
    for x in range(N):
        for y in range(N):              #모든 나라에 대해 그룹확인
            if check[x][y]==1:continue  #이미 그룹화 되었는지를 체크
            union,aver=bfs(x,y)
            if len(union)>1:
                flg=True
                for i,j in union:
                    A[i][j]=aver
                    check[i][j]=1
                    #city[i][j]=aver
    #A=city
    if not flg: break
    cnt+=1
print(cnt)
