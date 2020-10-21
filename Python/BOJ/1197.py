import sys
from collections import defaultdict
r=sys.stdin.readline
V,E=map(int,r().split())
g_info=[]
for _ in range(E):
    s,e,c=map(int,r().split())
    g_info.append([s-1,e-1,c])
class Disjset():
    def __init__(self,n):
        self.parent={}
        self.rank={}
        for i in range(n):
            self.parent[i]=i
            self.rank[i]=0
    def find(self,v):#루트노드를 찾자
        #다른 루트노드가 존재하면 재귀적으로 최상위 노드를 찾음
        if self.parent[v]!=v:
            self.parent[v]=self.find(self.parent[v])
        return self.parent[v]
    def union(self, root1, root2):
        if self.rank[root1]>self.rank[root2]:
            self.parent[root2]=root1
        else:
            self.parent[root1]=root2
            if self.rank[root1]==self.rank[root2]:
                self.rank[root2]+=1
def kruskal(n, info):
    minimum_w=0
    disjset=Disjset(n)
    for data in sorted(info,key=lambda x:x[2]):
        v,u,w=data
        root1=disjset.find(v)
        root2=disjset.find(u)
        if root1!=root2:
            disjset.union(root1,root2)
            minimum_w+=w
    return minimum_w
print(kruskal(V,g_info))