import sys
r=sys.stdin.readline
for _ in range(int(r())):
    N=int(r())
space=[]
for _ in range(N):
    space.append(list(map(int,r().split())))
INF=int(10e9)
dist=[[INF]*N for _ in range(N)]
dist[0][0]=space[0][0]