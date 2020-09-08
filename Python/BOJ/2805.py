import sys
from collections import Counter
r=sys.stdin.readline
N,M=map(int,r().split())
woods=Counter(map(int,r().split()))
def cnt_wood(woods, h):
    tmp=0
    for wood,cnt in woods.items():
        if wood>h:
            tmp+=(wood-h)*cnt
    return tmp
lo,hi=0,max(woods)
while lo <= hi:
    mid = (lo+hi)//2
    wood=cnt_wood(woods,mid)
    if wood >=M:
        result = mid
        lo = mid + 1
    else:
        hi = mid -1
print(result)
