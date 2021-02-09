import sys
r=sys.stdin.readline
N=int(r())
soldier=list(map(int,r().split()))
dp=[0]*N
#dp[n] -> n번째병사까지 남아있는 최대의 병사 수
ans=1
for i in range(N):
    dp[i]=1
    for j in range(i):
        if soldier[i]<soldier[j] and dp[j]+1>dp[i]:
            dp[i]=dp[j]+1
            ans=max(ans,dp[i])
print(N-ans)
