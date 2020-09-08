import sys
r=sys.stdin.readline
for _ in range(int(r())):
    arr=list(map(int,r().split()))
    print(sorted(arr)[-3])