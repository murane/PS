import sys,heapq
r=sys.stdin.readline
N=int(r())
lst=[[] for _ in range(N+1)]
for _ in range(N):
    deadline,cup=map(int,r().split())
    lst[deadline].append(cup)
heap=[]
ans=0
for i in range(N,0,-1):
    for cup in lst[i]:
        heapq.heappush(heap,(-cup))
    if heap:
        cur=-heapq.heappop(heap)
        ans+=cur
print(ans)