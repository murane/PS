import sys,heapq
r=sys.stdin.readline
N,D=map(int,r().split())
node=[]
shortCut=dict()
for _ in range(N):
    s,e,l=map(int,r().split())
    if 0<=s<=D:
        node.append(s)
    if 0<=e<=D:
        node.append(e)
    if 0<=s<=D and 0<=e<=D:
        if (s,e) in shortCut and shortCut[(s,e)]>l:
            shortCut[(s,e)]=l
        elif (s,e) not in shortCut:
            shortCut[(s,e)]=l
        
node.extend([0,D])
node=list(set(node))
node.sort()
g=[[] for _ in range(D+1)]

for i in range(len(node)-1):
    S,E=node[i],node[i+1]
    g[S].append([E,E-S])
for k,v in shortCut.items():
    S,E=k
    g[S].append((E,shortCut[k]))

INF=sys.maxsize
dist=[INF]*(len(node)+1)
dist[0]=0
def dikstra(N):
    q=[]
    heapq.heappush(q,(0,N))
    while q:
        curDist,curNode=heapq.heappop(q)
        if dist[node.index(curNode)]<curDist:#이미 더 빠른 지점을 탐색함
            continue
        for nxtNode,nxtDist in g[curNode]:
            if dist[node.index(nxtNode)]>curDist+nxtDist:
                dist[node.index(nxtNode)]=curDist+nxtDist
                heapq.heappush(q,(curDist+nxtDist,nxtNode))

dikstra(0)
print(dist[node.index(D)])