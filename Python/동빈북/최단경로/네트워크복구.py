import sys
r=sys.stdin.readline
N,M=map(int,r().split())
network=[[] for _ in range(N+1)]
for _ in range(M):
    A,B,C=map(int,r().split())
    network[A].append((B,C))
    network[B].append((A,C))

