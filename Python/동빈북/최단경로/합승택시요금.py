import sys
from collections import defaultdict
def solution(n, s, a, b, fares):
    INF=sys.maxsize
    answer = INF
    dist=[[INF]*(n+1) for _ in range(n+1)]
    for start,end,cost in fares:
        dist[start][end]=cost
        dist[end][start]=cost
    for i in range(1,n+1):
        dist[i][i]=0
    for m in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dist[i][m]+dist[m][j]<dist[i][j]:
                    dist[i][j]=dist[i][m]+dist[m][j]
    def get_dist(mid):
        return dist[s][mid]+dist[mid][a]+dist[mid][b]
    for i in range(1,n+1):
        answer=min(answer,get_dist(i))
    return answer