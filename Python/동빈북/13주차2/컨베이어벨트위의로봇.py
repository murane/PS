import sys
from collections import deque
r=sys.stdin.readline
N,K=map(int,r().split())
belts=deque(list(map(int,r().split())))
robots=deque([False]*N)
step=0
while True:
    step+=1
    belts.rotate(1)
    robots.rotate(1)
    if robots[N-1]==True:
        robots[N-1]=False
    for i in range(N-2,0,-1):
        if robots[i] and not robots[i+1] and belts[i+1]>0:
            robots[i]=False
            robots[i+1]=True
            belts[i+1]-=1
    if robots[N-1]==True:
        robots[N-1]=False
    robots[0]=False
    if belts[0]>0:
        robots[0]=True
        belts[0]-=1
    if belts.count(0)>=K:
        break
print(step)