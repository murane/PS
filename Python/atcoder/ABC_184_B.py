import sys
r=sys.stdin.readline
N,X=map(int,r().split())
S=r().strip()
for ch in S:
    if ch=='o':
        X+=1
    else:
        if X!=0:
            X-=1
print(X)