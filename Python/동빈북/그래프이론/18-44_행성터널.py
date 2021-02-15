import sys

def calCost(x,y):
    return min(abs(x[0]-y[0]),abs(x[1]-y[1]),abs(x[2]-y[2]))

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

if __name__ == "__main__":
    r=sys.stdin.readline
    N=int(r())
    planets=[]
    mapping={}
    for i in range(N):
        planets.append(list(map(int,r().split())))
        mapping[tuple(planets[i])]=i
    g_info=[]
    planets.sort(key=lambda x: x[0])
    for i in range(N-1):
        a,b=planets[i],planets[i+1]
        u=mapping[tuple(a)]
        v=mapping[tuple(b)]
        g_info.append([u,v,calCost(a,b)])
    planets.sort(key=lambda y: y[1])
    for i in range(N-1):
        a,b=planets[i],planets[i+1]
        u=mapping[tuple(a)]
        v=mapping[tuple(b)]
        g_info.append([u,v,calCost(a,b)])
    planets.sort(key=lambda z: z[2])
    for i in range(N-1):
        a,b=planets[i],planets[i+1]
        u=mapping[tuple(a)]
        v=mapping[tuple(b)]
        g_info.append([u,v,calCost(a,b)])
    print(kruskal(N,g_info))