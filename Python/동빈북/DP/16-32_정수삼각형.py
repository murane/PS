import sys
r=sys.stdin.readline
n=int(r())
triangle=[]
for _ in range(n):
    triangle.append(list(map(int,r().split())))
dp=triangle[0]
for i in range(n-1):
    tmp=[]
    for j in range(len(triangle[i+1])):
        cur=triangle[i+1][j]
        if j==0:
            tmp.append(dp[0]+cur)
        elif j==len(triangle[i+1])-1:
            tmp.append(dp[-1]+cur)
        else:
            tmp.append(max(dp[j-1]+cur,dp[j]+cur))
    dp=tmp
print(max(dp))