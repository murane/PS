import sys
from itertools import combinations
r=sys.stdin.readline
N,S=list(map(int,r().split()))
integers=list(map(int,r().split()))
cnt=0
"""
for i in range(1,N+1):
    for seq in combinations(integers,i):
        if sum(seq)==S:
            cnt+=1
"""
def comb(arr,r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in comb(arr[i+1:],r-1):
                yield [arr[i]]+next
for i in range(1,N+1):
    for seq in comb(integers,i):
        if sum(seq)==S:
            cnt+=1
print(cnt)
