import sys
from collections import Counter
r=sys.stdin.readline
rr=sys.stdin.readlines
r()
Nlist=rr()
counter=Counter(Nlist)
tmp=[]
for k,v in counter.items():
    if v==2:
        tmp.append(k.strip())
print(len(tmp))
for st in sorted(tmp):
    print(st)

