import sys
r=sys.stdin.readline
N,M=map(int,r().split())
INF=int(10e9)
dist=[[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    start,end=map(int,r().split())
    dist[start][end]=1

for i in range(1,N+1):
    dist[i][i]=0
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
ans=0
for i in range(1,N+1):
    flg=True
    for j in range(1,N+1):
        if dist[i][j]==INF and dist[j][i]==INF:
            flg=False
            break
    if flg:
        ans+=1
print(ans)