import sys,heapq
from collections import defaultdict
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
    if find(house,a)!=find(house,b):
        union(house,a,b)
        selected.append((c,a,b))
        tmpTree[a].append(b)
        tmpTree[b].append(a)
tot=sum([x[0] for x in selected])
while True:
    c,a,b=selected.pop()
    if len(tmpTree[a])>1 and len(tmpTree[b])>1:
        print(tot-c)
        break