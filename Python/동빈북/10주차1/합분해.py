import sys
r=sys.stdin.readline

N,K=map(int,r().split())
MOD=10**9
dp=[[0]*K for _ in range(N+1)]

for i in range(N+1):
    #0~i까지 1개를 더해서 i가 나오는 경우의 수
    #자기 자신이므로 1개
    dp[i][1]=1
    #0~i까지 2개를 더해서 i가 나오는 경우의 수
    #i+1
    dp[i][2]=i+1
    
    for j in range(1,K+1):
        if j==1:

def sol(n,k):
    if dp[n][k]!=0:
        return dp[n][k]
    
    #calc something
    dp[n][k]= ~~

    return dp[n][k]

print(sol(n,k))