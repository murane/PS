import sys
input = sys.stdin.readline
dp=[[0 for col in range(14+1)] for row in range(14+1)]
def recur(k,n):
    if k==1:
        return int(n*(n+1)/2)
    else:
        sum=0
        if dp[k][n]:
            return dp[k][n]
        else:
            for i in range(1,n+1):
                sum+=recur(k-1,i)
            dp[k][n]=sum
            return sum
T= int(sys.stdin.readline())
for i in range(T):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    print(recur(k,n))
