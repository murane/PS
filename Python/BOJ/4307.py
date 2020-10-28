import sys
r=sys.stdin.readline
for _ in range(int(r())):
    l,n=map(int,r().split())
    rod=[]
    for _ in range(n):
        rod.append(int(r()))
    fast,slow=0,0
    for leng in rod:
        fast=max(fast,min(leng,l-leng))
        slow=max(slow,max(leng,l-leng))
    print(fast,slow)
