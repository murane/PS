#3개씩 놓으면서 상하좌우로 체크하는게 
#연구소랑 유사하게 백트래킹하는 느낌이 왔따
import sys
from itertools import combinations
from collections import deque
r=sys.stdin.readline
N=int(r())
bokdo=[]
for _ in range(N):
    bokdo.append(list(r().split()))
blank=[]
teacher=[]
#장애물을 삽입할 공백과 bfs를 진행할 선생을 저장해놓는다
for i in range(N):
    for j in range(N):
        if bokdo[i][j]=='T':
            teacher.append((i,j))
        if bokdo[i][j]=='X':
            blank.append((i,j))
def bfs():
    q=deque()
    for x,y in teacher:
        #각방향으로만 진행하게 한다
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            q.append((x,y,(dx,dy)))
    while q:
        x,y,dxy=q.popleft()
        nx,ny=x+dxy[0],y+dxy[1]
        if not 0<=nx<N or not 0<=ny<N:continue
        if bokdo[nx][ny]=='O':continue
        #학생에 닿으면 이번 장애물 시행은 실패
        if bokdo[nx][ny]=='S':return False
        q.append((nx,ny,dxy))
    return True
for a,b,c in combinations(blank,3):
    bokdo[a[0]][a[1]]='O'
    bokdo[b[0]][b[1]]='O'
    bokdo[c[0]][c[1]]='O'
    #한번이라도 성공하면 YES
    if bfs():
        print("YES")
        exit(0)
    bokdo[a[0]][a[1]]='X'
    bokdo[b[0]][b[1]]='X'
    bokdo[c[0]][c[1]]='X'
print("NO")
#N^2중 3개를 뽑는 조합은 N^6의 복잡도를 가지고 
#각 시행별로 진행하는 bfs는 노드당 4번씩이므로 4N^2으로 근사해보면..
#대략 4N^8정도?
#공간부하는 