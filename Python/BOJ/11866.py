import sys
from collections import deque
r=sys.stdin.readline
N,K=list(map(int,r().split()))
josepus=[]
DQ=deque([x for x in range(1,N+1)])
cursor=0
while DQ:
    DQ.rotate(-(K-1))
    josepus.append(DQ[0])
    DQ.popleft()
print("<",end="")
print(", ".join(map(str,josepus)),end="")
print(">",end="")

