##바이러스를 시뮬레이팅했더니 시간이 오래걸림..
##bfs를 통해 효과적으로 구해보자
import sys
from collections import deque
r=sys.stdin.readline
N,K=map(int,r().split())
sihumguan=[]
for _ in range(N):
    sihumguan.append(list(map(int,r().split())))
virus=list()
#일단 바이러스 파악
for i in range(N):
    for j in range(N):
        if sihumguan[i][j]!=0:
            virus.append((i,j))
#번호순으로 정렬
virus.sort(key=lambda x: sihumguan[x[0]][x[1]])
S,X,Y=map(int,r().split())
def bfs():
    q=deque()
    q.extend(virus)
    time=0
    #그대로 bfs를 진행하면 시간을 알 수 없으니 tmp_q를 통해
    #한스텝씩 진행한다.
    while time<S:
        time+=1
        tmp_q=deque()
        while q:
            x,y=q.popleft()
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                nx,ny=x+dx,y+dy
                if not 0<=nx<N or not 0<=ny<N:continue
                if sihumguan[nx][ny]!=0:continue
                sihumguan[nx][ny]=sihumguan[x][y]
                tmp_q.append((nx,ny))
        q.extend(tmp_q)
bfs()
print(sihumguan[X-1][Y-1])
#최대 N^2개의 노드의 4개의 엣지를 순회한다 생각하면 약 16만번?
#공간부하는 원본 시험관 배열에서 크게 벗어나지 않는다.