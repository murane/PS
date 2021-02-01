import sys
r=sys.stdin.readline
N=int(r())
dp=[0,0,1,1]+[-1]*N
def jump(n):
    if dp[n]!=-1:
        return dp[n]
    else:
        #연산을 적용한 1과 나머지를 통해 -1을 표현하여 최소값을 구하자
        dp[n]=1+min(jump(n//2)+n%2,jump(n//3)+n%3,jump(n//5)+n%5)
        return dp[n]
print(jump(N))