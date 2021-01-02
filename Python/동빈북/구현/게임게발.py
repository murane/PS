import sys
r=sys.stdin.readline
N,M=map(int,r().split())
X,Y,di=map(int,r().split())
cur=(X-1,Y-1)
tb={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
Map=[]
for _ in range(N):
    Map.append(list(map(int,r().split())))
ans=0
