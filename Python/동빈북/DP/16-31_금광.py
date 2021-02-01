import sys
r=sys.stdin.readline
def sol(x,y):
    #메모
    if dp[x][y]!=-1:
        return dp[x][y]
    #기저사례
    if y==m-1:
        dp[x][y]=mine[x][y]
        return dp[x][y]
    lst=[]
    if x>0:
        lst.append((x-1,y+1))
    if x<n-1:
        lst.append((x+1,y+1))
    lst.append((x,y+1))
    #lst의 x,y좌표를 sol에 매핑한 최대값 + 현재 금이 dp[x][y]
    dp[x][y]=mine[x][y]+max(map(sol,[x[0] for x in lst],[x[1] for x in lst]))
    return dp[x][y]

for _ in range(int(r())):
    n,m=map(int,r().split())
    lst=list(map(int,r().split()))
    #1차원 -> 2차원
    mine=[lst[i*m:i*m+m] for i in range(n)]
    #dp[i][j] -> i,j에서부터 진행한 최대값
    dp=[[-1]*m for _ in range(n)]
    for i in range(n):
        sol(i,0)#각 행별로 시행
    #각 행중에 최대값
    print(max([dp[i][0] for i in range(n)]))