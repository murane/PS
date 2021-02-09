import sys
from collections import deque
r=sys.stdin.readline

N,M=map(int,r().split())
ans=0
visit=[[False]*M for _ in range(N)]
ice=[]
def bfs(x,y):
    visit[x][y]=True
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<M and 0<=ny<N and not visit[nx][ny] and ice[nx][ny]==1:
                q.append((nx,ny))
                visit[nx][ny]=True
for _ in range(N):
    ice.append(list(map(int,r().split())))
#모든 좌표에 대해 방문하지 않고 얼음이면 bfs를 진행
for i in range(M):
    for j in range(N):
        if ice[i][j]==1 and not visit[i][j]:
            bfs(i,j)
            #한번 bfs를 진행하면 같은 컴포넌트는 방문처리가 되어 한덩이로 처리됨
            ans+=1
print(ans)
#M*N번의 루프 안에서 M*N개의 정점을 정점당 최대 4방향으로 탐색하므로
#4MN번의 연산으로 근사할 수 있을것 같다.
#그래프 처리와 방문 처리에 2MN의 공간이 필요하다

