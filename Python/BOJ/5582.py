import sys
r=sys.stdin.readline
def LCS(A,B):
    dp=[[0]*(len(B)+1) for _ in range(len(A)+1)]
    ans=0
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if A[i-1]==B[j-1]:
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j-1]+1
                if dp[i][j]>ans:
                    ans=dp[i][j]
    return ans
print(LCS(r().strip(),r().strip()))