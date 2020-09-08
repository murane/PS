import sys
r=sys.stdin.readline
N=int(r())
divs=list(map(int,r().split()))

if len(divs)==1:
    print(divs[0]**2)
else:
    divs = sorted(divs)
    print(divs[0]*divs[-1])