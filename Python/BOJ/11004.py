import sys
r=sys.stdin.readline
N,K=map(int,r().split())
arr=list(map(int,r().split()))
print(sorted(arr)[K-1])