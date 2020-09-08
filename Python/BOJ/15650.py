import sys
from itertools import combinations

def comb(arr, r):
    arr = sorted(arr)
    res=[]
    def gen(picked):
        if len(picked)==r:
            res.append(list(picked))
            return
        else:
            start=arr.index(picked[-1])+1 if picked else 0
            for i in range(start, len(arr)):
                picked.append(arr[i])
                gen(picked)
                picked.pop()
    gen([])
    return res

r = sys.stdin.readline
N, M = list(map(int,r().split()))

res = comb(range(1,N+1), M)
#res = list(combinations(range(1,N+1),M))
for item in res:
    for num in item:
        print(num,end=" ")
    print("")
