import sys
r=sys.stdin.readline
for _ in range(int(r())):
    n,k=map(int,r().split())
    a=list(map(int,r().split()))
    a.sort()
    print(sum(a[-(k+1):]))