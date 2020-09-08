import sys
from collections import Counter
rr=sys.stdin.readlines
r=sys.stdin.readline
max=10000
arr={}
for _ in range(int(r())):
    tmp = int(r())
    try:
        arr[tmp]+=1
    except KeyError:
        arr[tmp]=1
for key in sorted(arr.keys()):
    print('\n'.join([str(key)]*arr[key]))