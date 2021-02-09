import sys
r=sys.stdin.readline
N=int(r())
INF=sys.maxsize
nalary=[-INF]+list(map(int,r().split()))
dp=[[None]*2 for _ in range(N+1)]
boss=[-1,-1]+list(map(int,r().split()))
tree=[[] for _ in range(N+1)]
sys.setrecursionlimit(10**9)
for i in range(2,N+1):
    tree[boss[i]].append(i)
del boss
#dp[n][0] -> n번사원을 포함안했을때 최대 날라리 지수
#dp[n][1] -> n번사원을 포함했을때 최대 날라리 지수
def dfs(n):
    for child in tree[n]:
        dfs(child)
    if not tree[n]:
        dp[n][0]=0
        dp[n][1]=nalary[n]
    else:
        dp[n][0]=sum(list(max(dp[x]) for x in tree[n]))
        dp[n][1]=nalary[n] + sum(list(dp[x][0] for x in tree[n]))
def backtrack(n,flag):
    #n번노드를 포함하는 경우
    if flag:
        for nxt in tree[n]:
            backtrack(nxt,0)
    else:
        for nxt in tree[n]:
            if dp[nxt][0]>dp[nxt][1]:
                backtrack(nxt,0)
            else:
                backtrack(nxt,1)
                lst.append(nxt)
dfs(1)
print(dp[1][1],dp[1][0])
lst=[1]
backtrack(1,True)
print(*sorted(lst),-1)
lst=[]
backtrack(1,False)
print(*sorted(lst),-1)
