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
        cnt+=min(n//i,N)
    return cnt

while lo<=hi:
    mid=(lo+hi)//2
    if sol(mid)>=K:
        ans=mid
        hi=mid-1
    else:
        lo=mid+1
print(ans)
        