import sys
r=sys.stdin.readline
K,N=map(int,r().split())
lensun=[]
for _ in range(K):
    lensun.append(int(r()))
def counter(leng):
    cnt=0
    for lens in lensun:
        cnt+=(lens//leng)
    return cnt
lo=1
hi=max(lensun)
res=0
while lo<=hi:
    mid=(hi+lo)//2
    cnt=counter(mid)
    if cnt<N:
        hi=mid-1
    elif cnt>=N:
        lo=mid+1
        res=mid
print(res)