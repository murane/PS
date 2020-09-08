import sys
r=sys.stdin.readline
N=int(r())
arr=list(map(int,r().split()))
tmp=[0]*2002
for num in arr:
    tmp[num+1000]=1
for i in range(2002):
    if tmp[i]==1:
        print(i-1000,end=' ')