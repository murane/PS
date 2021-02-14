import sys,heapq
from collections import defaultdict
r=sys.stdin.readline
N,M=map(int,r().split())
def find(X):
    if house[X]==X:
        return X
    house[X]=find(house[X])
    return house[X]
def union(X,Y):
    X=find(X)
    Y=find(Y)
    if X==Y:
        return
    if X>Y:
        house[X]=Y
    else:
        house[Y]=X

gil=[]
house=[0]+list(range(1,N+1))
heapq.heapify(gil)
for _ in range(M):
    a,b,c=map(int,r().split())
    heapq.heappush(gil,(c,a,b))

tmpTree=defaultdict(list)
selected=[]
while gil:
    tmp=heapq.heappop(gil)
    c,a,b=tmp[0],tmp[1],tmp[2]
    if find(a)!=find(b):
        union(a,b)
        selected.append((c,a,b))
        tmpTree[a].append(b)
        tmpTree[b].append(a)
tot=sum([x[0] for x in selected])
while True:
    c,a,b=selected.pop()
    if len(tmpTree[a])>1 and len(tmpTree[b])>1:
        print(tot-c)
        break