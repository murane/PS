import sys
from collections import deque
r=sys.stdin.readline
N,M,K,X=map(int,r().split())
doro=[[] for _ in range(N+1)]
for _ in range(M):
    A,B=map(int,r().split())
    doro[A].append(B)
#X노드에 대한 거리배열을 생성한다
dist=[-1]*(N+1)
dist[X]=0
lst=[]
def bfs(curNode):
    q=deque()
    q.append(curNode)
    while q:
        curNode=q.popleft()
        if dist[curNode]>K:return
        for nextNode in doro[curNode]:
            if dist[nextNode]==-1:
                dist[nextNode]=dist[curNode]+1
                if dist[nextNode]==K:
                    lst.append(nextNode)
                q.append(nextNode)
#bfs로 최단거리가 보장되므로 해당하는 지점을 출력한다.
bfs(X)
if not lst:
    print(-1)
else:
    print('\n'.join(map(str,sorted(lst))))
#최악의 경우 모든 정점에서 모든 간선을 점검해야 하므로
#N+M만큼의 복잡도를 가진다.
#공간은 인접 그래프에서 M에 비례하는 공간을 차지한다.