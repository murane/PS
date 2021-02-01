import sys
r=sys.stdin.readline
N=int(r())
sik=list(map(int,r().split()))
dp=[[-1]*2 for _ in range(N)]
for i in range(N):
    if i==0:
        dp[0][0]=0
        dp[0][1]=sik[0]
    else:
        dp[i][0]=dp[i-1][1]
        dp[i][1]=dp[i-1][0]+sik[i]
print(max(dp[N-1]))
