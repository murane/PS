import sys
r=sys.stdin.readline
t=int(r())
for _ in range(t):
    p,q=map(int,r().split())
    for i in range(1,int(p**0.5)+1):
        if p%i==0:
            x=p//i
            if x%q!=0:
                print(x)
                break