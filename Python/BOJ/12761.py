import sys
from collections import deque
r=sys.stdin.readline
A,B,N,M=map(int,r().split())
visit=[-1]*100001
q=deque()
q.append((N,0))
visit[N]=0
while q:
    cur,cnt=q.popleft()
    if cur==M: 
        print(cnt)
        exit(0)
    tmp=[cur+1,cur-1,cur+A,cur-A,cur+B,cur-B,cur*A,cur*B]
    for next in tmp:
        if next<0 or next>10**5: continue
        if visit[next]==-1:
            visit[next]=cnt+1
            q.append((next,cnt+1))
