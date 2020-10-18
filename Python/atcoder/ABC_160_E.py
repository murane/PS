import sys
r=sys.stdin.readline
X,Y,A,B,C=map(int,r().split())
Red=list(map(int,r().split()))
Green=list(map(int,r().split()))
White=list(map(int,r().split()))
Red.sort(reversed=True)
Green.sort(reversed=True)
White.sort(reversed=True)
