import sys
from functools import lru_cache
from collections import defaultdict
r=sys.stdin.readline
sys.setrecursionlimit(10**9)
N=int(r())
g=defaultdict(set)
for _ in range(N-1):
    a,b=map(int,r().split())
    g[a].add(b)
    g[b].add(a)
    #양방향 그래프 구성
tree=[-1]+[(0,0)]*N#1번~N번까지 부모,레벨 설정
#leafs=[]
def buildTree(parent):
    #if not g[parent]:
    #    leafs.append(parent)
    for node in g[parent]:
        tree[node]=(parent,tree[parent][1]+1)
        g[node].discard(parent)
        buildTree(node)
        #dfs로 그래프탐색하여 노드별 부모와 레벨 설정
buildTree(1)
@lru_cache()
def LCA(a,b):
    if a==b:
        return a
    #기저사례
    else:
        if tree[a][1]>tree[b][1]:#b가 더 높은 레벨일경우
            return LCA(tree[a][0],b)
        elif tree[a][1]<tree[b][1]:#a가 더 높은 레벨일경우
            return LCA(a,tree[b][0])
        else:#레벨이 같은경우
            return LCA(tree[a][0],tree[b][0])
M=int(r())
res=[]
for _ in range(M):
    a,b=map(int,r().split())
    a,b=min(a,b),max(a,b)
    res.append(LCA(a,b))
for num in res:
    print(num)