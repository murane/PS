import sys
r=sys.stdin.readline
A,B,C=map(int,r().split())
if A**2+B**2<C**2:
    print("Yes")
else:
    print("No")