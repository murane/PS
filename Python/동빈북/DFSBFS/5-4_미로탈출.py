import sys
from collections import deque
r=sys.stdin.readline
N,M=map(int,r().split())
miro=[]
for _ in range(N):
    miro.append(list(map(int,r().strip())))
#방문배열이 없어도 1이 길이 되므로 1을 4방향으로 탐색하며
#1씩 올려가며 경로를 계산할 수 있다.
def bfs(x,y):
    q=deque([(x,y)])
    while q:
        x,y=q.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny=x+dx,y+dy
            if not 0<=nx<N or not 0<=ny<M:continue
            if miro[nx][ny]!=1:continue
            q.append((nx,ny))
            miro[nx][ny]=miro[x][y]+1
            if (nx,ny) == (N-1,M-1): return
bfs(0,0)
print(miro[N-1][M-1]-1)
#1의 갯수*4번의 연산이 최악의 경우 필요하다
#즉 4MN
#NM만큼의 공간을 사용한다