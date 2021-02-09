import sys
r=sys.stdin.readline
n,m=map(int,r().split())
square=[]
for _ in range(n):
    square.append(list(map(int,r().strip())))
dp=dict()
ans=0
def sol(x1,x2,y1,y2):
    global ans
    if x1==x2 and y1==y2:
        return square[x1][y1]
    key=(x1,y1,(x2-x1+1)*(y2-y1+1))
    if  key in dp:
        return dp[key]
    elif (x1,x2,y1,y2) not in dp:
        tmp=[]
        tmp.append(sol(x1+1,x2,y1+1,y2))
        tmp.append(sol(x1+1,x2,y1,y2-1))
        tmp.append(sol(x1,x2-1,y1+1,y2))
        tmp.append(sol(x1,x2-1,y1,y2-1))
        dp[key]= 0 if 0 in tmp else (x2-x1+1)*(y2-y1+1)
    ans=max(ans,dp[key])
    return dp[key]
if n==m:
    sol(0,n-1,0,m-1)
else:
    if n>m:
        for i in range(n-m+1):
            sol(i,m-1+i,0,m-1)
    else:
        for i in range(m-n+1):
            sol(0,n-1,i,n-1+i)
print(ans)
