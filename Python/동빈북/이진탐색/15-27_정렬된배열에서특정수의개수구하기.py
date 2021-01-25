import sys,bisect
r=sys.stdin.readline
N,x=map(int,r().split())
seq=list(map(int,r().split()))
l=bisect.bisect_left(seq,x)
r=bisect.bisect_right(seq,x)
print(r-l if 0<r-l<=N else -1)
