import sys
r=sys.stdin.readline
A,B,C,D=map(int,r().split())
if B<C or D<A:
    print("No")
else:
    print("Yes")