import sys
r=sys.stdin.readline
N,M=map(int,r().split())
INF=int(10e9)
graph=[[INF]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    graph[i][i]=0
    #자기자신으로의 거리는 0
for _ in range(M):
    a,b=map(int,r().split())
    graph[a][b]=1
    graph[b][a]=1
    #양방향 1로 세팅
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[j][i]=graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
            #양방향 거리 갱신
X,K=map(int,r().split())
ans=graph[1][K]+graph[K][X]
#1 -> K + K -> X 가 답이됨
if ans>=INF:
    print(-1)
else:
    print(ans)