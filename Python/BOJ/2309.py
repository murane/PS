import sys
from itertools import combinations
r=sys.stdin.readlines
dwarfs=list(map(int,r()))
s=sum(dwarfs)
flg=True
for two in combinations(dwarfs,2):
    if s-sum(two)==100:
        flg=False
        for dwarf in sorted(dwarfs):
            if dwarf not in two:
                print(dwarf)
    if not flg:
        break