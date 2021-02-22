import sys
r=sys.stdin.readline

D=int(r())
MOD=10**9+7
dp=[0]*8
dp[0]=1
#정보, 전산, 미래, 신양, 한경, 진리, 학관, 형남
#0 -> 1 2
#1-> 2,3
#2-> 1,3
#3 -> 1,2,4,5
#4 -> 2,3,5,7
#5 -> 3,4,6
#6 -> 5,7
#7 -> 6,6

for _ in range(D):
    tmp=dp[:]
    tmp[0]=dp[1]+dp[2]
    tmp[1]=dp[0]+dp[2]+dp[3]
    tmp[2]=dp[0]+dp[1]+dp[3]+dp[4]
    tmp[3]=dp[1]+dp[2]+dp[4]+dp[5]
    tmp[4]=dp[2]+dp[3]+dp[5]+dp[7]
    tmp[5]=dp[3]+dp[4]+dp[6]
    tmp[6]=dp[5]+dp[7]
    tmp[7]=dp[4]+dp[6]
    dp=tmp

print(dp[0]%MOD)