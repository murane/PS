import sys
from string import ascii_lowercase
from itertools import combinations
r=sys.stdin.readline
L,C=map(int,r().split())
alpabets=r().split()
mo="aeiou"
for word in combinations(sorted(alpabets),L):
    flg=False
    cnt=0
    for ch in word:
        if ch in mo:
            flg=True
        else:
            cnt+=1
    if flg and cnt>=2:
        print(''.join(word))