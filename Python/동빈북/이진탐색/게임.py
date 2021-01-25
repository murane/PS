import sys
r=sys.stdin.readline
X,Y=map(int,r().split())
Z=int((Y*100)/X)
if Z>=99:
    print(-1)
    exit(0)
def winRate(X,Y):
    return int((Y*100)/X)
lo,hi=1,10**9
ans=-1
while lo<=hi:
    mid=(lo+hi)//2
    cur=winRate(X+mid,Y+mid)
    if cur!=Z:
        hi=mid-1
        ans=mid
    else:
        lo=mid+1
print(ans)