import sys
r=sys.stdin.readline
sys.setrecursionlimit(10**9)
M,N=map(int,r().split())
gido=[]
for _ in range(M):
    gido.append(list(map(int,r().split())))
dp=[[0]*N for _ in range(M)]
dp[0][0]=1
def sol(x,y):
    if dp[x][y]!=0:
        return dp[x][y]
    cnt=0
    if x>0 and gido[x][y]<gido[x-1][y]:
        cnt+=sol(x-1,y)
    if x<M-1 and gido[x][y]<gido[x+1][y]:
        cnt+=sol(x+1,y)
    if y>0 and gido[x][y]<gido[x][y-1]:
        cnt+=sol(x,y-1)
    if y<N-1 and gido[x][y]<gido[x][y+1]:
        cnt+=sol(x,y+1)
    dp[x][y]+=cnt
    return dp[x][y]
sol(M-1,N-1)
print(dp[M-1][N-1])