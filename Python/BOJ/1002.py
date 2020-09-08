import sys
r=sys.stdin.readline
for _ in range(int(r())):
    x1,y1,r1,x2,y2,r2=list(map(int,r().split()))
    if r1>r2:
        r1,r2=r2,r1
    dist = ((x1-x2)**2+(y1-y2)**2)**0.5
    if r1==r2:
        if dist==0:
            print(-1)
        elif r1+r2==dist:
            print(1)
        elif r1+r2<dist:
            print(0)
        elif r1+r2>dist:
            print(2)
    else:
        if r1+r2<dist or r2-r1>dist:
            print(0)
        elif r1+r2==dist or r2-r1==dist:
            print(1)
        elif r1+r2>dist and r2-r1<dist:
            print(2)