import sys
r=sys.stdin.readline
N,M=map(int,r().split())
dduck=list(map(int,r().split()))
lo,hi=1,2*(10**9)
ans=0
while lo<=hi:
    mid=(lo+hi)//2
    res=sum(list(x-mid for x in dduck if x>=mid))
    if res>=M:
        lo=mid+1
        ans=mid
    else:
        hi=mid-1
print(ans)