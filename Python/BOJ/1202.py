import sys
from collections import defaultdict
import heapq
r=sys.stdin.readline
N,K=map(int,r().split())
gems=[]
for _ in range(N):#무게, 가격
    M,V=map(int,r().split())
    gems.append([M,V])
gems.sort(key=lambda x: x[0])
bags=[]
for _ in range(K):
    bags.append(int(r()))
bags.sort()
ans=0
i=0
heap=[]
for bag in bags:
    while i<N and gems[i][0]<=bag:
        heapq.heappush(heap,-gems[i][1])
        i+=1
    if heap:
        ans+=(-heapq.heappop(heap))
print(ans)




