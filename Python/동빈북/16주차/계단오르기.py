import sys
r=sys.stdin.readline
N=int(r())
floor=[0]
for _ in range(N):
    floor.append(int(r()))
dp = [[0,0] for _ in range(N+1)]
for i,x in enumerate(floor):
    if i==0:continue
    elif i==1:
        dp[i][0]=dp[i-1][1]+floor[i]
    elif i==2:
        dp[i][0]=dp[i-1][0]+floor[i]
        dp[i][1]=floor[i]
    else:
        dp[i][0]=dp[i-1][1]+floor[i]
        dp[i][1]=max(dp[i-2])+floor[i]
print(max(dp[N]))