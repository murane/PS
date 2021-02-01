import sys
r=sys.stdin.readline
n,k=map(int,r().split())
coin=[]
dp=[0]*(k+1)   
for _ in range(n):
    coin.append(int(r()))
dp[0]=1
for i in coin:
    for j in range(i,k+1):
        if j-i>=0:
            dp[j]+=dp[j-i]
print(dp[k])