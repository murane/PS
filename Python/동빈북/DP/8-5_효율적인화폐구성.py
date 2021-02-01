import sys
r=sys.stdin.readline
N,M=map(int,r().split())
coin=[]
dp=[0]+[10001]*10000
for _ in range(N):
    coin.append(int(r()))
    dp[coin[-1]]=1
for x in coin:#각 동전별로
    cur=x
    while cur<=M:
        #dp배열의 cur원을 만드는 경우를
        #최소값으로 새로 갱신해나간다.
        dp[cur]=min(dp[cur-x]+1,dp[cur])
        cur+=x
if dp[M]!=10001:
    print(dp[M])
else:
    print(-1)

