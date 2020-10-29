import sys
from collections import deque, defaultdict
r=sys.stdin.readline
N,M=map(int,r().split())
hutgan=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,r().split())
    hutgan[a].append(b)
    hutgan[b].append(a)
distDict=defaultdict(list)
def bfs(v):
    visit=[0]*(N+1)
    q=deque()
    q.append((v,0))
    visit[v]=1
    while q:
        cur,dist=q.popleft()
        for node in hutgan[cur]:
            if not visit[node]:
                visit[node]=1
                q.append((node,dist+1))
                distDict[dist+1].append(node)
    num=max(list(distDict.keys()))
    return min(distDict[num]), num, len(distDict[num])

print(*bfs(1))


