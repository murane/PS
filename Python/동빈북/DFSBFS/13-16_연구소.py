import sys
from itertools import combinations
from collections import deque
r=sys.stdin.readline
N,M=map(int,r().split())
lab=[]
for _ in range(N):
    lab.append(list(map(int,r().split())))
blank=[]
virus=[]
#빈칸과 바이러스를 저장
for i in range(N):
    for j in range(M):
        if lab[i][j]==0:
            blank.append((i,j))
        elif lab[i][j]==2:
            virus.append((i,j))
#lst에는 각 시행별로 안전구역을 저장
lst=[]
def bfs():
    q=deque()
    q.extend(virus)
    tmp=set()
    global cnt1,cnt2
    while q:
        x,y=q.popleft()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny=x+dx,y+dy
            if not 0<=nx<N or not 0<=ny<M:continue
            #0을 탐색하면 tmp에 저장하고 중복은 배제
            if lab[nx][ny]!=0 or (nx,ny) in tmp: continue
            tmp.add((nx,ny))
            q.append((nx,ny))
    #미리구한 공백에서 바이러스로 전염된갯수를 빼면 안전구역
    lst.append(len(blank)-len(tmp))
#빈칸 3개를 뽑는 조합을 완전탐색
for a,b,c in combinations(blank,3):
    lab[a[0]][a[1]]=1
    lab[b[0]][b[1]]=1
    lab[c[0]][c[1]]=1
    bfs()
    lab[a[0]][a[1]]=0
    lab[b[0]][b[1]]=0
    lab[c[0]][c[1]]=0
#벽으로 삼은 3개를 보정
print(max(lst)-3)
#빈칸중 3개를 뽑는 시행에 대해 bfs를 돌리므로
#대략 (N*M)^3에  N*M이 곱해져 (NM)^4으로 근사할 수 있지 않을까..?
#lst가 가장 큰 공간을 차지하는데 최대값만 취하면 효율적일것 같다.