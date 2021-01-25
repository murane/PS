import sys
import bisect
r=sys.stdin.readline
def LIS(lst):
    tmp=[]
    for n in lst:
        if not tmp:
            tmp.append(n)
        else:
            if tmp[-1]>=n:
                idx=bisect.bisect_left(tmp,n)
                tmp[idx]=n
            else:
                tmp.append(n)
    return len(tmp)
while True:
    try:
        N=int(r())
        print(LIS(list(map(int,r().split()))))
    except:
        break
    