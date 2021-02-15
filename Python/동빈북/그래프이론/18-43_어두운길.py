import sys,heapq
r=sys.stdin.readline
N,M=map(int,r().split())
def find(lst,X):
    if lst[X]==X:
        return X
    lst[X]=find(lst,lst[X])
    return lst[X]
def union(lst,X,Y):
    X=find(lst,X)
    Y=find(lst,Y)
    if X==Y:
        return
    if X>Y:
        lst[X]=Y
    else:
        lst[Y]=X
house=list(range(N))
q=[]
heapq.heapify(q)
tot=0
cost=0
for _ in range(M):
    X,Y,Z=map(int,r().split())
    heapq.heappush(q,(Z,X,Y))
    tot+=Z

while q:
    Z,X,Y=heapq.heappop(q)
    if find(house,X)!=find(house,Y):
        union(house,X,Y)
        cost+=Z

print(tot-cost)