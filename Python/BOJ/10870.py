import sys
r=sys.stdin.readline
sys.setrecursionlimit(10000)
dp=[0,1]+[-1]*10000
def fibo(n):
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fibo(n-1)+fibo(n-2)
        return dp[n]
    
print(fibo(int(r())))
