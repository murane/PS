import sys
from collections import Counter
r=sys.stdin.readline
for _ in range(int(r())):
    n=int(r())
    arr=list(map(int,r().split()))
    counter=Counter(arr)
    res=[]
    for k,v in counter.items():
        if v==1:
            res.append(k)
    if res:
        res.sort()
        if len(res)==1 or res[0]!=res[1]:
            print(arr.index(res[0])+1)
    else:
        print(-1)