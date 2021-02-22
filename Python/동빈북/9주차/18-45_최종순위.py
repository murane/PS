import sys
r=sys.stdin.readline
for _ in range(int(r())):
    n=int(r())
    lastYear=list(map(int,r().split()))
    swap=[]
    for _ in range(int(r())):
        a,b=map(int,r().split())
        swap.append((a,b))
    
