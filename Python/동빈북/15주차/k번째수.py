import sys,bisect
r=sys.stdin.readline
N=int(r())
K=int(r())
arr=[]
lo,hi=1,N**2
ans=0
def sol(n):
    cnt=0
    for i in range(1,N+1):
        l,r=1*i,N*i
        if l<=n<=r:
            arr=[x*i for x in range(1,N+1)]
            idx=bisect.bisect_right(arr,n)
            cnt+=idx
        else:
            continue
    return cnt

while lo<hi:
    mid=(lo+hi)//2
    if sol(mid)>K:
        hi=mid-1
    else:
        lo=mid+1
        ans=mid+1
print(ans)
        