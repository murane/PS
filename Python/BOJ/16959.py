import sys
from collections import deque
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
cur=1
def bfs(x,y):
    q=deque([(x,y)])


    
while cur<N**2:
    curPos=coord[cur]
    nextPos=coord[cur+1]
    dx,dy=nextPos[0]-curPos[0],nextPos[1]-curPos[1]

    cur+=1