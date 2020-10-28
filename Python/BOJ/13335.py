import sys
from collections import deque
r=sys.stdin.readline
n,w,L=map(int,r().split())
truck=deque(list(map(int,r().split())))
bridge=deque()
arrive=deque()
t=0
on_bridge_weight=0
while len(arrive)!=n:#
    for i in range(len(bridge)): 
        bridge[i][1]+=1
    if bridge and bridge[0][1]==w+1:
        on_bridge_weight-=bridge[0][0]
        arrive.append(bridge.popleft())
    if truck and truck[0]+on_bridge_weight <= L: #트럭이 올라가도 되는경우
        on_bridge_weight+=truck[0]
        bridge.append([truck.popleft(),1])
    t+=1

print(t)




