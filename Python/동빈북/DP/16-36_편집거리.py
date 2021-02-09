import sys
r=sys.stdin.readline
A=r().split()
B=r().split()
if len(A)>len(B):
    A,B=B,A
dp=[[-1]*len(A) for _ in range(len(B))]
