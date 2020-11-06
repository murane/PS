import sys
from collections import defaultdict
r=sys.stdin.readline
for _ in range(int(r())):
    N,M,W=map(int,r().split())
    doro=defaultdict(set)
    doroFilter=dict()
    #두 지점을 연결하는 도로가 한개 이상일 수 있기 때문에
    #(S,E) dict으로 최소값을 취한다
    for _ in range(M):
        S,E,T=map(int,r().split())
        if (S,E) in doroFilter and doroFilter[(S,E)]>T:
            doroFilter[(S,E)]=T
    for k,v in doroFilter.items():
        S,E=k
        doro[S].add((E,T))
        doro[E].add((S,T))
    #웜홀은 음수가중치의 단방향 그래프로 생성한다.
    for _ in range(W):
        S,E,T=map(int,r().split())
        doro[S].add((E,-T))

INF=sys.maxsize
#모든 정점에 대해 최단거리를 구한다
visit=[False]*(N+1)
for v in range(1,N+1):
    #사이클을 확인한 그룹은 방문하지 않는다
    if not visit[v]:
        for i in range(N):
            


