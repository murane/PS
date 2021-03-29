import sys
from collections import deque
r=sys.stdin.readline
N,L=map(int,r().split())
lst=[]
left=0
right=0
l=0
for i in range(N):
    vl=int(r())
    if vl>0:
        right=max(right,L-vl)
    else:
        left=max(left,abs(vl))
        l+=1
    lst.append((abs(vl),i+1))
lst.sort(key=lambda x : x[0])

l_ant=lst[l-1]
r_ant=lst[l]
if left> right:
    print(f'{l_ant[1]} {left}')
else:
    print(f'{r_ant[1]} {right}')

https://keykat7.blogspot.com/2020/06/BJ-2136.html