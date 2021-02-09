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
        if up<=F and visit[up]==-1:
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
