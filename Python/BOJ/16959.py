import sys
r=sys.stdin.readline
N=int(r())
chess=[]
for _ in range(N):
    chess.append(list(map(int,r().split())))
coord=dict()
for i in range(N):
    for j in range(N):
        coord[chess[i][j]]=(i,j)
time=0
