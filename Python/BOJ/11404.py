import sys
r=sys.stdin.readline
n=int(r())
m=int(r())
INF=sys.maxsize
cost=[[INF]*(n+1) for _ in range(n+1)]
vertex=[[-1]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s,e,c=map(int,r().split())
    cost[s][e]=c
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            cost[i][j]=0
        if cost[i][j]!=INF:
            vertex[i][j]=i

for mid in range(1,n):
    for i in range(1,n):
        for j in range(1,n):
            if cost[i][mid] + cost[mid][j] < cost[i][j]:
                cost[i][j]=cost[i][mid] + cost[mid][j]
for i in range(1,n+1):
    for j in range(1,n+1):
        print(cost[i][j],end=" ")
    print("")