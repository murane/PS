import sys
from itertools import combinations
r=sys.stdin.readline
while True:
    lst=list(map(int,r().split()))
    if lst[0]==0:
        break
    for seq in combinations(lst[1:],6):
        print(" ".join(list(map(str,seq))))
    print("")
