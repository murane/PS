import sys
r=sys.stdin.readline
while True:
    line=list(map(int,r().split()))
    line.sort()
    a,b,c=line
    if a==0 and b==0 and c==0:
        break
    else:
        if c**2==a**2+b**2:
            print("right")
        else:
            print("wrong")