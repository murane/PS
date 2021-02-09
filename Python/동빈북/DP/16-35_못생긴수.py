import sys
import heapq
r=sys.stdin.readline
n=int(r())
q=[1]
dp=set()
heapq.heapify(q)
while len(dp)<n:
    cur=heapq.heappop(q)
    for i in [2,3,5]:
        if cur*i not in dp:
            heapq.heappush(q,cur*i)
            dp.add(cur)        
print(sorted(list(dp))[n-1])