import sys
r=sys.stdin.readline
rr=sys.stdin.readlines
n=int(r())
V=[-1]+list(map(int,r().split()))
g=[[] for _ in range(n+1)]
parent=[0 for _ in range(n+1)]
for line in rr():
    s,e=map(int,line.split())
    g[s].append(e)
    g[e].append(s)
#dp[i][0] => i를 루트로하는 서브트리에서 i를 포함하지 않았을때 크기
#dp[i][1] => i를 루트로하는 서브트리에서 i를 포함했을때 크기
dp=[[-1]*2 for _ in range(n+1)]

def dfs(cur):

    res=0

    for sub in g[cur]:
        if sub not in visited:
            
