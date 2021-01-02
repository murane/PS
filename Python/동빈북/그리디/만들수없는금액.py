import sys
r=sys.stdin.readline
N=int(r())
coin=list(map(int,r().split()))
coin.sort()
target=1
for x in coin:
    if target<x:
        break
    target+=x
print(target)
