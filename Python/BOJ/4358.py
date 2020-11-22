import sys
from collections import Counter
r=sys.stdin.readline
rr=sys.stdin.readlines
lst=list(map(str.strip,rr()))
counter=Counter()
for wood in lst:
    counter[wood]+=1
total=len(lst)
lst=list(set(lst))
for wood in sorted(lst):
    per=counter[wood]/total*100
    print(f'{wood} {per:.4f}')