import sys
r=sys.stdin.readline
N=int(r())
dp={1:0,2:1,3:1}
def jump(n):
    if n in dp:
        return dp[n]
    else:
        dp[n]=1+min(jump(n//2)+n%2,jump(n//3)+n%3)
        return dp[n]

print(jump(N))