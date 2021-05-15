import sys
r=sys.stdin.readline
N=int(r())
A=list(map(int,r().split()))
B=list(map(int,r().split()))
l,r=1,1000
for i in range(N):
    if A[i]>B[i]:continue
    l=max(l,A[i])
    r=min(r,B[i])
if r-l+1<=0:
    print(0)
else:
    print(r-l+1)
