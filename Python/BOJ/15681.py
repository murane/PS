import sys
r=sys.stdin.readline
N,R,Q=map(int,r().split())
edge=[set() for _ in range(N+1)]
sys.setrecursionlimit(10**9)
for _ in range(N-1):
    a,b=map(int,r().split())
    edge[a].add(b)
    edge[b].add(a)
tree=[-1]*(N+1)
dp=[0]*(N+1)
def make_tree(parent):
    for child in edge[parent]:
        tree[child]=parent
        edge[child].discard(parent)
        make_tree(child)
def dfs(node):
    if len(edge[node])==0:
        dp[node]=1
        return dp[node]
    else:
        tmp=0
        for child in edge[node]:
            tmp+=dfs(child)
        dp[node]=tmp+1
    return dp[node]
make_tree(R)
dfs(R)
for _ in range(Q):
    print(dp[int(r())])
