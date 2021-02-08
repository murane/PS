import sys
r=sys.stdin.readline
n=int(r())
m=int(r())
INF=sys.maxsize
cost=[[INF]*n for _ in range(n)]
for _ in range(m):
    s,e,c=map(int,r().split())
    if cost[s-1][e-1]!=INF:
        cost[s-1][e-1]=min(c,cost[s-1][e-1]) 
    else:
        cost[s-1][e-1]=c
for i in range(n):
    for j in range(n):
        if i==j:
            cost[i][j]=0
for mid in range(n):
    for i in range(n):
        for j in range(n):
            if cost[i][mid] + cost[mid][j] < cost[i][j]:
                cost[i][j]=cost[i][mid] + cost[mid][j]
for i in range(n):
    for j in range(n):
        if cost[i][j]==INF:
            print(0,end=" ")
        else:
            print(cost[i][j],end=" ")
    print("")