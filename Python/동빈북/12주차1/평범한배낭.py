import sys
r=sys.stdin.readline
N,K=map(int,r().split())
bag=[]
for _ in range(N):
    W,V=map(int,r().split())
    bag.append([W,V])

dp = [0]*(K+1)

for w,v in bag:
    for x in range(w,min(K+1,2*w)):
        dp[x]=max(dp[x],dp[x-w]+v)

print(dp[K])