import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x,y=list(map(int,input().split()))
    d=y-x
    if d==1:
        print("1")
    elif d==2:
        print("2")
    else:
        Max=2
        dist=2
        while True:
            dist+=1
            if dist%2==1:
                tmp=dist//2+1
                Max=tmp*(tmp+1)/2+(tmp-1)*(tmp)/2
            else:
                tmp=dist/2
                Max=tmp*(tmp+1)
            if Max >= d:
                break
        print(dist)
