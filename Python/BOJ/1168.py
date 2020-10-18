import sys
from collections import deque
r=sys.stdin.readline
N,K=map(int,r().split())
q=deque(list(range(1,N+1)))
res='<'
while q:
    q.rotate(-(K-1))
    if len(q)>1:
        res+=(str(q.popleft())+", ")
    else:
        res+=(str(q.popleft())+">")
print(res)
