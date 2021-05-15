import sys
r=sys.stdin.readline

#n개의 공을 놓고 1~n의 위치중 k 번째에 특별한 공을 놓는다
#그후 m번의 swap을 실행한다
#i번째 교환에서 xi,yi번째 공을 교환한다.
#m번의 swap중 fake가 있을 수 있다. fake의 수는 0~m일 수 있다.

UNREACHABLE=2*10**5
n,m,k=map(int,r().split())
dp=[UNREACHABLE]*(n+1)
dp[k]=0
for _ in range(m):
    x,y=map(int,r().split())
    X,Y=dp[x],dp[y]
    dp[x]=min(X+1,Y)
    dp[y]=min(X,Y+1)

print(*[x if x!=UNREACHABLE else -1 for x in dp[1:]])
