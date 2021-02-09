import sys,bisect
r=sys.stdin.readline
N,x=map(int,r().split())
seq=list(map(int,r().split()))
# l=bisect.bisect_left(seq,x)
# r=bisect.bisect_right(seq,x)
def upper_bound(lst,target):
    lo,hi=0,len(lst)
    while lo<hi:
        mid=(lo+hi)//2
        if target<lst[mid]:
            hi=mid
        else:
            lo=mid+1
    return lo
def lower_bound(lst,target):
    lo,hi=0,len(lst)
    while lo<hi:
        mid=(lo+hi)//2
        if lst[mid]<target:
            lo=mid+1
        else:
            hi=mid
    return lo
l=lower_bound(seq,x)
r=upper_bound(seq,x)
print(r-l if 0<r-l<=N else -1)
