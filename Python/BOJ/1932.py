import sys
r=sys.stdin.readline
n=int(r())
triangle=[]
for _ in range(n):
    triangle.append(list(map(int,r().split())))
dp=triangle[0]  #초기값
for i in range(n-1):
    tmp=[]      #dp 리스트를 한 행마다 유지
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

#입력값인 n개의 행을 순회하여 dp연산이 이루어지므로
#시간복잡도는 n^2이며 공간또한 저장된 triangle의 범위를 벗어나지 않는다.