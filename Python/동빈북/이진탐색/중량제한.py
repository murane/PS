import sys
import heapq
from collections import defaultdict,deque
r=sys.stdin.readline
N,M=map(int,r().split())
islands=defaultdict(int)
tmp=defaultdict(int)
for _ in range(M):
    A,B,C=map(int,r().split())
    A,B=min(A,B),max(A,B)
    tmp[(A,B)]=C
    if tmp[(A,B)]<C:
        tmp[(A,B)]=C
for k,v in tmp.items():
    x,y=k
    islands[x]=(y,v)
    islands[y]=(x,v)
tx,ty=map(int,r().split())
parent=list(range(N))
def find(x):
    if parent[x]==x:
        return x
    parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    X=find(x)
    Y=find(y)
    if X==Y:
        return
    else:
        parent[Y]=X

    