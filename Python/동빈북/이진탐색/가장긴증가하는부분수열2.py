import sys
import bisect
r=sys.stdin.readline
N=int(r())
arr=list(map(int,r().split()))
dp=[arr[0]]
tmp=[]
for i in range(N):
    if arr[i]>dp[-1]:
        dp.append(arr[i])
        tmp.append(len(dp)-1)
    else:
        idx=bisect.bisect_left(dp,arr[i])
        dp[idx]=arr[i]
        tmp.append(idx)
print(len(dp))
ans=[]
i=len(dp)
for idx in range(len(tmp)-1,-1,-1):
    if tmp[idx] == i-1:
        ans.append(arr[idx])
        i-=1
print(*reversed(ans))