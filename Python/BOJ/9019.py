import sys
from collections import deque
r=sys.stdin.readline
def D(n):
    return (n*2)%10000
def S(n):
    return (n-1)%10000
def L(n):
    return (n*10)%10000+n//1000
def R(n):
    return (n%10)*1000+n//10
tb={0:"D",1:"S",2:"L",3:"R"}
def bfs(start,target):
    visited[start]=1
    q=deque()
    q.append(start)
    while q:
        num = q.popleft()
        d,s,l,r=D(num),S(num),L(num),R(num)  
        for i,v in enumerate([d,s,l,r]):
            if visited[v]!=1:
                route[v]=route[num]+tb[i]
                visited[v]=1
                q.append(v)
        if visited[target]!=0:
            return route[target]
for _ in  range(int(r())):
    A,B=map(int,r().split())
    visited=[0]*10000
    route=[""]*10000
    print(bfs(A,B))
