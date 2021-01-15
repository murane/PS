import sys
import heapq
r=sys.stdin.readline
cards=[]
for _ in range(int(r())):
    cards.append(int(r()))
heapq.heapify(cards)
if len(cards)==1:
    print(0)
else:
    ans=0
    while len(cards)>1:
        cur=heapq.heappop(cards)+heapq.heappop(cards)
        ans+=cur
        heapq.heappush(cards,cur)
    print(ans)