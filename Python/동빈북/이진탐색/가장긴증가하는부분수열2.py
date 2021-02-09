import sys
import bisect
r=sys.stdin.readline
N=int(r())
arr=list(map(int,r().split()))
# dp=[1]*N
# #n^2의 시간복잡도
# for i in range(N):
#     for j in range(i):
#         if arr[i]>arr[j]:
#             dp[i]=max(dp[i],dp[j]+1)
# print(max(dp))
dp=[arr[0]]

for i in range(N):
    if arr[i]>dp[-1]:
        dp.append(arr[i])
    else:
        idx=bisect.bisect_left(dp,arr[i])
        dp[idx]=arr[i]
print(len(dp))