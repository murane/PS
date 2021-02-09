import sys
from collections import defaultdict
<<<<<<< HEAD
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

if __name__ == '__main__':
    n=7
    s=3
    a=4
    b=1
    fares=[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    solution(n,s,a,b,fares)
    
=======
r=sys.stdin.readline
n,m=map(int,r().split())
subjs=defaultdict(list)
in_cnt=[0]*(n+1)
out_cnt=[0]*(n+1)
for _ in range(m):
    u,v=map(int,r().split())
    in_cnt[v]+=1
    out_cnt[v]+=1
    subjs[u].append(v)
need_sub=int(r())
start_lst=[]
for i in range(1,len(in_cnt)):
    if in_cnt[i]==0:
        start_lst.append(i)

>>>>>>> dacae1c1569dc4de981c69564ab60c50a80e62ff
