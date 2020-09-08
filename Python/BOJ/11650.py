import sys
from operator import itemgetter
r=sys.stdin.readline
rr=sys.stdin.readlines
N=int(r())
coords=[]
for _ in range(N):
    (x, y) = list(map(int, r().split()))
    coords.append((x,y))
coords.sort(key=itemgetter(0,1))
for tup in coords:
    print(f'{tup[0]} {tup[1]}')