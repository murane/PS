import sys,heapq
sys.setrecursionlimit(10**6)
r=sys.stdin.readline
N=int(r())
C=list(map(int,r().split()))
AB=[[] for _ in range(N+1)]
for _ in range(N-1):
    A,B=map(int,r().split())
    AB[A].append(B)
    AB[B].append(A)

visit=[False]*(N+1)
visit[1]=True
ans=set()
ans.add(1)
ck=set()
ck.add(C[0])
def dfs(N:int,ck:set):
    for nxt in AB[N]:
        if not visit[nxt]:
            visit[nxt]=True
            if C[nxt-1] not in ck:
                ans.add(nxt)
                ck.add(C[nxt-1])
                dfs(nxt,ck)
                if C[nxt-1] in ck:
                    ck.remove(C[nxt-1])
            else:
                dfs(nxt,ck)
            
dfs(1,ck)
print('\n'.join(map(str,sorted(list(ans)))))
