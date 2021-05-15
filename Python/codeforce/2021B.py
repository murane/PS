import sys
r=sys.stdin.readline
N,D,H=map(int,r().split())
ans=0
for _ in range(N):
    d,h=map(int,r().split())
    p=(H-h)/(D-d)
    q=H-p*D
    ans=max(ans,q)
print(ans)