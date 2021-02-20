import sys
r=sys.stdin.readline
for _ in range(int(r())):
    n,k=map(int,r().split())
    lst=list(map(int,r().split()))
    st=set(lst)
    if k in st:
        print("YES")
    lst.sort()
    diff=0
    for i in range(len(lst)-1):
        diff=min(diff,abs(lst[i]-lst[i+1])
    