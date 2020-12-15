import sys
import bisect
r=sys.stdin.readline
N=int(r())
k=int(r())
ans=0
def solution(num,N):
    if num==1:
        return 1
    elif num==N**2:
        return N**2
    else:
        LR=[1,N]
        cnt=0
        for i in range(1,N+1):
            L,R=LR[0]*i,LR[1]*i
            if num<L:
                break
            elif L<=num<=R:
                cnt+=(num//i)
            elif L<num:
                cnt+=N
        return cnt
lo,hi=1,N**2
while lo<=hi:
    mid=(lo+hi)//2
    if mid>3 and mid%3!=0:
        while mid%3!=0:
            mid+=1
    tmp=solution(mid,N)
    if tmp==k or hi==mid or lo==mid:
        break
    elif k<tmp:
        hi=mid
    elif tmp<k:
        lo=mid-1
print(mid)
