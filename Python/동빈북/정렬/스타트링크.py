#현재층에서 목표층으로의 최소 버튼횟수를 구하므로
#BFS로 최단거리를 보장할 수 있다.
import sys
from collections import deque
r=sys.stdin.readline
F,S,G,U,D=map(int,r().split())
visit=[-1]*(F+1)
def bfs(x):
    q=deque([x])
    visit[x]=0
    while q:
        cur=q.popleft()
        up=cur+U
        #방문하지 않은 층을 오르내린다.
        if up<=F and visit[up]==-1:
            #visit배열은 -1을 초기값으로 버튼을 누른횟수를 저장
            visit[up]=visit[cur]+1
            q.append(up)
        down=cur-D
        if down>=1 and visit[down]==-1:
            visit[down]=visit[cur]+1
            q.append(down)
        if visit[G]!=-1:
            return True
    return False
if bfs(S):
    print(visit[G])
else:
    print("use the stairs")
#100만개의 층을 한번씩 탐색할 수 있으므로
#100만*상수 범위의 시간복잡도를 가진다.