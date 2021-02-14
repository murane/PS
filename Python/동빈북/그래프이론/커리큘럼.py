import sys
from collections import deque
r=sys.stdin.readline
N=int(r())
lecture=[[] for _ in range(N+1)]
lecTime=[0]*(N+1)
degree=[0]*(N+1)
ans=[0]*(N+1)
for i in range(1,N+1):
    lst=list(map(int,r().split()))
    lecTime[i]=lst[0]
    degree[i]+=len(lst[1:-1])
    for j in lst[1:-1]:
        lecture[j].append(i)
q=deque()
for i in range(1,N):
    if degree[i]==0:
        q.append(i)
        ans[i]=lecTime[i]

while q:
    cur=q.popleft()
    for i in lecture[cur]:
        ans[i]=max(ans[i],lecTime[i]+ans[cur])
        degree[i]-=1
        if degree[i]==0:
            q.append(i)
for i in range(1,N+1):
    print(ans[i])
