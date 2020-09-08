import sys
r=sys.stdin.readline
N,M=map(int,r().split())
tb=[list(map(int,r())) for _ in range(N)]

for y in range(len(tb)):
    for x in range(len(tb[0])-3):
        