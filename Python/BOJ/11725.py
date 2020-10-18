import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
r=sys.stdin.readline
N=int(r())
tree=defaultdict(set)
for _ in range(N-1):
    a,b=map(int,r().split())
    tree[a].add(b)
    tree[b].add(a)
myParent=[-1]+[0]*N
def traverse(parent):
    lst = tree[parent]
    if not lst:
        return
    for node in lst:
        tree[node].discard(parent)
        myParent[node]=parent
        traverse(node)
traverse(1)
for i in range(2,N+1):
    print(myParent[i])