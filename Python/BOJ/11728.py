import sys
r=sys.stdin.readline
N,M=map(int,r().split())
A=list(map(int,r().split()))
B=list(map(int,r().split()))
A.extend(B)
print(' '.join(map(str, sorted(A))))