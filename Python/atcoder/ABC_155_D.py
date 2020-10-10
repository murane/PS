import sys
from collections import defaultdict
r=sys.stdin.readline
N,K=map(int,r().split())
A=list(map(int,r().split()))
A.sort()
tb=dict()
for i in range(len(A)-1):
    #i번째의 최소, 최대, 갯수
    tb[i]=(A[i]*A[i+1],A[i]*A[-1],len(A)-(i+1))

k=0
for k,v in tb.items():
    start,end,cnt=v
    