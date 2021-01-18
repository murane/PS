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
    #카드뭉치가 1개 남을때까지
    #두 묶음을 합쳐서 넣는다
    while len(cards)>1:
        cur=heapq.heappop(cards)+heapq.heappop(cards)
        ans+=cur
        heapq.heappush(cards,cur)
    print(ans)

