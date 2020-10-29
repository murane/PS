import sys
from collections import deque
r=sys.stdin.readline
N,K=map(int,r().split())
visit=[-1]*1000001
def bfs(cur):
    q=deque()
    q.append(cur)
    visit[cur]=0
    if cur==K: 
        return visit[cur]
    while q:
        cur=q.popleft()
        curtime=visit[cur]
        for _next in [cur+1,cur-1,cur*2]:
            if _next<0 or _next>100000: continue
            if visit[_next]==-1:
                visit[_next]=curtime+1
                q.append(_next)
                if _next==K:
                    return visit[_next]

print(bfs(N))